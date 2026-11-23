# Decisions log

## 2026-11-23 — Session 1 miss review (narrative eval, claude-sonnet-5-5)
Owner: Will Haynes

| Complaint | My label | Model | Call | Reason |
|---|---|---|---|---|
| 24148120 fraud account opened in business name, frozen | high | medium | Label stands; rule gap | Business-linked fraud is high visibility: potential deep relationship. |
| 22760485 Chime closed account, payroll will bounce | high | medium | Model miss | Blocked paycheck is high under the existing rule. |
| 23484039 disabled, low-income customer locked out over $24 fee | high | medium | Label stands; rule gap | Reputational risk: vulnerable customer losing access. |
| 23537280 $490 dispute open, accounts delinquent | route to human | no | Model miss | Repeated failed contact on a non-trivial amount is on the route list. |
| 23121634 $4 fees after promised waiver | low / Reg DD / no human | medium / UDAAP / human | Label stands | Small-dollar fee dispute; "lie" wording does not make it UDAAP. |

Rule changes to apply in Session 2 (proposed, pending Will's approval of exact wording):
1. Urgency high: fraud or identity theft involving a business account.
2. Urgency high: a vulnerable customer (disabled, low income, older American, servicemember) who has lost access to their account, even over a small fee.
3. Reg flag: small-dollar fee disputes stay Reg DD even when the customer calls it a lie or misleading; UDAAP needs a pattern or material harm.

Note: rules 1 and 2 add bank-risk (relationship, reputation) to urgency, not only customer harm. Deliberate choice.

## 2026-11-23 — Pass bars set (Will)
- High-urgency catch rate: 95% (now 25/28 = 89%, FAIL)
- Overall urgency: 85% (now 56/65 = 86%, pass)
- Reg flag: 90% (now 61/65 = 94%, pass)
- Route to human: 95% (now 63/65 = 97%, pass)
Missing a real crisis is the costliest error, so high-urgency catch has the strictest bar.
