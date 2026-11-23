# Evals

## Baseline — claude-sonnet-5-5 (2026-11-05)
- urgency: 25/50
- reg: 30/50
- human: 33/50

## After labeling rules + golden update (2026-11-05)
- urgency: 26/50
- reg: 41/50
- human: 31/50

## Narrative eval — claude-sonnet-5-5 (2026-11-23)
Set: golden_narratives.csv (65 CFPB checking/savings narratives, Will's labels). Script: run_evals_narrative.py. Raw output: eval-run-2026-11-23.txt
- urgency: 56/65
- reg: 61/65
- human: 63/65
- high-urgency cases caught: 25/28 (3 called medium)
- Caveat: the urgency rules were tuned on this same set (2026-11-18), so this likely overstates performance on new complaints.

## Session 2 re-run — 3 rule changes from DECISIONS.md (2026-11-23)
Raw output: eval-run-2026-11-23-s2.txt
- urgency: 59/65 (was 56)
- reg: 59/65 (was 61)
- human: 65/65 (was 63)
- high-urgency cases caught: 26/28 (was 25; misses 22760485, 22792043)
- Fixed: 24148120, 23484039, 23121634, 23537280. New reg misses: 3 "None" fee/check cases now tagged Reg DD (side effect of the small-fee rule).
- Single run; model output varies run to run, so a 1-2 case swing may be noise.
