import json
from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel
import anthropic
import duckdb

load_dotenv()
client = anthropic.Anthropic()


class TriageResult(BaseModel):
    issue_category: str
    urgency: Literal["low", "medium", "high"]
    reg_flag: Literal["Reg E", "Reg DD", "Reg Z", "UDAAP", "None"]
    route_to_human: bool
    next_step: str


con = duckdb.connect()
golden = con.execute("SELECT * FROM read_csv_auto('golden_set.csv')").fetchall()

score = {"urgency": 0, "reg": 0, "human": 0}

for cid, company, issue, sub_issue, urgency, reg, human, notes in golden:
    prompt = f"""
    Return ONLY valid JSON matching this schema:
    {json.dumps(TriageResult.model_json_schema())}

    Bank: {company}
    Issue: {issue}
    Sub-issue: {sub_issue}
    Rules:
    - Deposits and withdrawals: default Reg E when money movement is involved (unauthorized, missing, or delayed funds).
    - Account closures: UDAAP when the customer claims unfair closure or no notice.
    Urgency:
    - high: unauthorized transactions, can't stop withdrawals, account opened without consent, money taken on the wrong day or for the wrong amount, funds not handled as instructed, and problems making or receiving payments.
    - medium: debit or ATM card problems, account closures (by the customer or the bank), problems accessing an account, and overdraft fees.
    - low: deposits and withdrawals, opening an account, banking errors, late or NSF fees, and advertised-terms complaints.
    """
    msg = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = next(b.text for b in msg.content if hasattr(b, "text")).strip().removeprefix("```json").removesuffix("```").strip()
    r = TriageResult.model_validate_json(raw)

    score["urgency"] += r.urgency == urgency
    score["reg"] += r.reg_flag == reg
    score["human"] += r.route_to_human == human
    if r.reg_flag != reg:
        print(f"MISS {cid}: you said {reg}, Claude said {r.reg_flag} ({sub_issue})")

print()
for k, v in score.items():
    print(f"{k}: {v}/{len(golden)}")