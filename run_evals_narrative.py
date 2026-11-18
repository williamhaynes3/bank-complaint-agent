import json
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel
import anthropic
import duckdb

load_dotenv()
client = anthropic.Anthropic()

ROOT = Path(__file__).resolve().parent
GOLDEN_PATH = ROOT / "golden_narratives.csv"

GUIDANCE = """
Judge from the customer's written narrative, not from the issue or sub-issue name alone.
When the story and the dropdown disagree, the story controls. Do not use a sub-issue-to-label lookup table.

Urgency:
- high: funds the customer needs now are missing, frozen, or inaccessible (rent, payroll, mortgage, food, medical, or essentially all of their money); unauthorized access is uncontained; a large unreimbursed loss remains (about $800 or more, or a smaller amount that is clearly their last funds); or imminent harm (eviction, missed mortgage today, no food). A large loss can still be high even if the customer initiated the payment.
- medium: a real unresolved problem that is not an immediate livelihood crisis, including a denied or pending dispute without an essential-expense crisis, modest fees or a modest negative balance, identity-theft account opening with little current loss of the customer's own funds, inability to close an account that may still accrue fees, adverse banking-history reporting after the balance was paid, or a deposit hold / delayed paycheck with inconvenience or living-expense pressure but no imminent harm.
- low: a promotional bonus or advertised term was not honored and no funds were seized; an after-the-fact fee-waiver request with the account otherwise usable; or a small fee or merchant-billing issue with no hardship.

Reg_Flag — pick one primary flag for the core harm in the narrative:
- Reg E: unauthorized electronic transfers (debit, ATM, ACH, P2P, bill pay, or account takeover); errors in electronic transfers (wrong amount or day, ATM deposit not credited, missing electronic credit); failed error investigation or clawback of provisional credit; failure to honor a stop-payment on a preauthorized EFT; debit/ATM overdraft opt-in or opt-out not honored.
- Reg DD: advertised deposit-account terms, APY, or bonuses not honored; available-balance representations that caused surprise NSF or overdraft fees; fee issues that turn on how the product or fee was disclosed.
- Reg Z: a credit product, line of credit, or overdraft line of credit attached to the deposit relationship; an unwanted credit product the customer cannot remove.
- UDAAP: account opened without consent; unfair account closure; unfair withholding of the customer's own funds, including a 100% hold plus a refusal to release living expenses or return the check; deceptive sales, forced add-on products, or bait-and-switch. Use UDAAP when unfairness or deception is the core harm.
- None: ordinary service or operational failures with no clear regulatory hook; a merchant billing fight on a purchase the customer authorized (overcharge, a fee that was supposed to be waived, defective goods, or a refund the merchant promised and did not pay) — that is None, not Reg E; payments the customer initiated even if a third party tricked them into sending the money (authorized-but-scammed), unless the bank's denial practice itself is the core unfairness.

Route_To_Human:
- TRUE when urgency is high; there is fraud, identity theft, or an account opened without consent; a vulnerable customer has unresolved funds or access harm (a servicemember or older-American tag alone is not enough if the only issue is a missed bonus or a small fee); roughly $1,000 or more is still missing or held; the bank broke a promise on an overdraft opt-out, even if the dollar amount is small; there is police, FTC, or attorney involvement; the case is potential UDAAP or has messy regulatory overlap; or an account closure is trapping funds or there is no working path to close or access the account.
- FALSE when urgency is low, the dollars are small, and there is a straightforward ops path (promotional bonus, small fee waiver, or a modest fee complaint that is not an opt-out or investigation failure); there is no fraud, no trapped essential funds, and no vulnerability-plus-harm.
- Medium urgency can go either way: TRUE for fraud, identity theft, a broken overdraft opt-out promise, repeated failed contact on a non-trivial amount, or regulatory complexity; FALSE for a routine small-fee or terms complaint.
""".strip()


class TriageResult(BaseModel):
    issue_category: str
    urgency: Literal["low", "medium", "high"]
    reg_flag: Literal["Reg E", "Reg DD", "Reg Z", "UDAAP", "None"]
    route_to_human: bool
    next_step: str


def as_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().upper() in {"TRUE", "T", "1", "YES"}


con = duckdb.connect()
golden = con.execute(
    """
    SELECT
        "Complaint ID",
        Company,
        Issue,
        "Sub-issue",
        Narrative,
        Urgency,
        Reg_Flag,
        Route_To_Human
    FROM read_csv_auto(?)
    """,
    [str(GOLDEN_PATH)],
).fetchall()

score = {"urgency": 0, "reg": 0, "human": 0}

for cid, company, issue, sub_issue, narrative, urgency, reg, human in golden:
    urgency = str(urgency).strip().lower()
    reg = str(reg).strip()
    human = as_bool(human)

    prompt = f"""
    Return ONLY valid JSON matching this schema:
    {json.dumps(TriageResult.model_json_schema())}

    Bank: {company}
    Issue: {issue}
    Sub-issue: {sub_issue}

    Customer narrative:
    {narrative}

    Rules:
    {GUIDANCE}
    """
    msg = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    text = next(b.text for b in msg.content if hasattr(b, "text"))
    try:
        # Grab the first JSON object and ignore anything Claude adds after it
        obj, _ = json.JSONDecoder().raw_decode(text[text.index("{"):])
        r = TriageResult.model_validate(obj)
    except Exception as e:
        print(f"PARSE FAIL {cid}: {e}")
        continue

    score["urgency"] += r.urgency == urgency
    score["reg"] += r.reg_flag == reg
    score["human"] += r.route_to_human == human

    if r.urgency != urgency:
        print(f"MISS urgency {cid}: you said {urgency}, Claude said {r.urgency} ({sub_issue})")
    if r.reg_flag != reg:
        print(f"MISS reg {cid}: you said {reg}, Claude said {r.reg_flag} ({sub_issue})")
    if r.route_to_human != human:
        print(f"MISS human {cid}: you said {human}, Claude said {r.route_to_human} ({sub_issue})")

print()
for k, v in score.items():
    print(f"{k}: {v}/{len(golden)}")
