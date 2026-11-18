# Narrative labeling guide — bank complaint triage

Use this guide to label checking or savings complaints from the **consumer's written narrative**, not from the CFPB issue or sub-issue dropdown alone. The sub-issue is a hint. When the story and the dropdown disagree, the story controls.

This golden set is a proof-of-concept. The 10 rows marked `Review=YES` were reviewed by Will on 2026-11-18; those labels are his decisions, and their Notes include `Reviewed by Will 2026-11-18`.

## Source of the complaints

The live CFPB Consumer Complaint Database stopped publishing narratives in September 2026 (Release 24; CFPB announcement of August 14, 2026). These rows come from the official [CFPB FOIA Narratives Archive](https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/), June and July 2026 full-record exports (`CCDB_Export_19_June_2026` and `CCDB_Export_20_July_2026`). August 2026 had no published checking/savings narratives. Every row is a real Complaint ID with its published, CFPB-scrubbed narrative (`XXXX` redactions are original). Product is "Checking or savings account." Narratives were limited to 300–2000 characters.

## Fields

| Field | Values |
| --- | --- |
| Urgency | `low` / `medium` / `high` |
| Reg_Flag | `Reg E` / `Reg DD` / `Reg Z` / `UDAAP` / `None` (pick one primary flag) |
| Route_To_Human | `TRUE` / `FALSE` |
| Review | `YES` on the 10 closest calls; `NO` otherwise |
| Notes | One-line rationale; on `Review=YES` rows, include `Reviewed by Will 2026-11-18` |

## Urgency — judge the story

Do not assign urgency from sub-issue alone. Weigh whether money is currently missing or inaccessible, hardship, vulnerability, dollar amount, and time sensitivity.

**High** when one or more of these is true:

- Funds the consumer needs now are missing, frozen, or inaccessible (rent, payroll, mortgage, food, medical bills, or essentially all of the consumer's money).
- Unauthorized access or fraud is still uncontained, or a large unreimbursed loss remains (~$800 or more, or a smaller amount that is clearly the consumer's last funds). A large loss can still be high even if the consumer initiated the payment (see authorized-but-scammed below).
- Imminent harm: eviction, missed mortgage, repossession, inability to buy food, or an account closure that is trapping a paycheck or rent money.
- A vulnerable consumer (older American, servicemember, disabled, homeless or recently homeless) has a *current* funds or access problem, not merely a past inconvenience.

**Medium** when the problem is real and unresolved, but not an immediate livelihood crisis:

- An unauthorized or error claim has already been reported and the card or login has been secured, but reimbursement is still denied or pending, and the narrative does not describe an essential-expense crisis.
- Fees or a modest negative balance, without a present inability to meet rent, food, or medical needs.
- Identity-theft account opening that has been frozen or declined, with little or no current loss of the consumer's own funds.
- Inability to close an account that may still accrue fees.
- Adverse banking-history reporting that blocks a new account, after the underlying balance has been paid.
- A deposit hold or delayed paycheck, even for a large amount, when the consumer is inconvenienced or under living-expense pressure but the narrative does not show imminent harm (eviction, no food, missed mortgage due today).

**Low** when the matter is after-the-fact, small, or mostly about terms:

- A promotional bonus or advertised term was not honored, and no funds were seized.
- A fee-waiver request after the fact, with the account otherwise usable.
- Small recurring charges or a modest fee with no hardship stated.

Dollar amount alone does not set the tier. Fifty dollars in overdraft fees with no hardship is low or medium. A few hundred dollars that stops a rent payment can be high.

## Reg_Flag — one primary flag

If two regulations could apply, choose the one that best matches the *core harm in the narrative*. Mention the runner-up in Notes.

**Reg E** (Electronic Fund Transfer Act / 12 CFR 1005)

- Unauthorized electronic fund transfers: debit card, ATM, ACH, P2P, bill pay, or account takeover used to send transfers.
- Errors in electronic transfers: wrong amount, wrong day, an ATM deposit not credited, or a missing electronic credit.
- Failed or inadequate error investigation, including denial without evidence or clawback of provisional credit.
- Failure to honor a stop-payment on a preauthorized EFT.
- Overdraft *opt-in / opt-out* for ATM and one-time debit card transactions (this is a Reg E rule, not just a fee-disclosure issue).

**Reg DD** (Truth in Savings / 12 CFR 1030)

- Deposit-account disclosures, advertised APY, bonuses, or promotional terms not honored.
- Available-balance representations that caused surprise NSF or overdraft fees.
- Overdraft or maintenance-fee issues that turn on how the product was advertised or how fees and availability were disclosed.

**Reg Z** (Truth in Lending / 12 CFR 1026)

- A credit product, line of credit, or overdraft *line of credit* attached to or opened with the deposit relationship.
- Billing disputes on that credit feature, or an unwanted credit product the consumer cannot remove.

**UDAAP** (unfair, deceptive, or abusive acts or practices)

- An account opened without consent (identity theft or a bank-initiated product the consumer did not want).
- Unfair account closure, or unfair withholding of the consumer's own funds — including after closure, and including a 100% hold with a refusal to release living expenses or return the check — especially without notice.
- Deceptive sales, forced add-on products, or bait-and-switch.
- Use UDAAP when the core harm is unfairness, deception, or abuse rather than a clean EFT error or a disclosure failure.

**None**

- Ordinary service or operational failures with no clear regulatory hook (for example, a software glitch that bounced a check, a small fee-waiver request, or a $10 check-cashing fee, with no disclosure or unauthorized-transfer issue).
- A **merchant billing fight** on a purchase the consumer authorized: the merchant overcharged, charged a fee that was supposed to be waived, sold defective goods, or promised a refund and did not pay it. That is `None`, not Reg E. Reg E covers unauthorized transfers and bank or ATM errors, not a disagreement with a merchant's bill.
- Funds-availability / Reg CC hold disputes, when that is the only legal hook and the withholding is not unfair. **Reg CC is not in this flag set.** If the bank also broke a stated availability promise, that can be Reg DD. If the withholding is unfair — for example a 100% hold plus a refusal to release living expenses or return the check — use **UDAAP**.
- Authorized payments the consumer initiated, even if a third party tricked them into sending the money. See the close-call rule below.

### Recurring close calls

**Merchant billing fights.** If the consumer authorized the card or Cash App payment and the dispute is with the merchant (overcharge, waived fee that was still collected, defective goods, refund promised but not paid), the flag is `None`, not Reg E. Urgency is usually low or medium unless the resulting negative balance or closure threat is a livelihood crisis.

**Authorized-but-scammed payments.** If the consumer initiated the transfer (typed the amount, scanned a barcode, confirmed a P2P send) and only later learned it was a scam, Reg E's "unauthorized" definition generally does not apply. Label `None` unless the bank's *investigation or denial practice* is the core unfairness, in which case consider UDAAP. If someone else took over the account or card and sent the money, that is Reg E. Urgency can still be **high** when a large amount is gone.

**Overdraft and NSF fees.**

- Available balance was shown as sufficient, or the fee/program disclosure is the issue → **Reg DD**.
- Debit/ATM overdraft opt-in or opt-out not honored → **Reg E**.
- Overdraft *line of credit* or other credit feature → **Reg Z**.
- Root event is an unauthorized transfer or a reversed provisional credit, and fees followed → primary **Reg E**; mention the fees in Notes.
- Repeated, stacked, or targeting-a-vulnerable-consumer fee practices, when unfairness is the core claim → **UDAAP**.
- "I just don't like this fee" after a true NSF, with no disclosure issue → **None**.

**Account closures and access problems.** No-notice closure or a closed account that traps a paycheck or rent money is usually **UDAAP**. An open Reg E claim that happens to sit on an account being closed stays **Reg E** if the disputed electronic transfers are the money at issue. "I can't close a zero-balance account and fees may accrue," with no working close path, is **UDAAP**.

**Bank setoff** (the bank takes funds to pay an alleged old debt) is not automatically Reg E. Prefer UDAAP if there was no notice or no documentation, or None if it reads as a contractual setoff dispute.

## Route_To_Human

**TRUE** when a person should see the case:

- Urgency is high.
- Fraud, identity theft, or an account opened without consent.
- A vulnerable consumer with *unresolved funds or access harm* (a servicemember or older-American tag alone is not enough if the only issue is a missed bonus or a small fee).
- Roughly $1,000 or more still missing or held.
- The consumer already tried the bank repeatedly and was denied or given conflicting answers, except on small, routine promo or fee-waiver issues. A broken promise on an overdraft opt-out can still go to a human even if the dollar amount is small.
- Police, FTC, or attorney involvement, or a live legal question (setoff authority, mixed permission, forced credit product).
- Potential UDAAP, or messy overlap between flags.
- Account closure that is trapping funds, or no working path to close or access the account.

**FALSE** when:

- Low urgency, small dollars, and a straightforward ops path: promotional bonus, small fee waiver, or a modest fee complaint that is not an opt-out or investigation failure.
- No fraud, no trapped essential funds, and no vulnerability-plus-harm.
- The bank is already resolving a minor issue and the consumer is mainly documenting it.

Medium urgency can go either way: route TRUE for fraud, identity theft, a broken overdraft opt-out promise, repeated failed contact on a non-trivial amount, or regulatory complexity; FALSE for a routine small-fee or terms complaint.

## How to use `Review=YES`

The 10 `YES` rows were the closest calls in the first draft and were reviewed by Will on 2026-11-18. Keep his labels. Additional rows added after that review are `Review=NO`.

## Suggested workflow

1. Read the narrative first, then glance at issue and sub-issue.
2. Assign urgency from current harm, not from the category name.
3. Assign one primary Reg_Flag from the core harm.
4. Assign Route_To_Human from the rules above.
5. If two labels are defensible, follow this guide and Will's reviewed examples; do not silently override a `Review=YES` row.
