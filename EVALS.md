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
