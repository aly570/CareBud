# CareBud rules for coding and design agents

Codex, Antigravity and any other agent that edits this repository follow these rules. The PR reviewer follows [CLAUDE.md](CLAUDE.md).

Read first: [README](README.md), [docs/units.md](docs/units.md), and docs/app-contract.md once U01 has merged.

## Work

1. One unit is one branch and one PR. Name the branch after the unit, for example `u03-patient-plan`. Title the PR with the unit ID and link the issue with `Closes #NUMBER`.
2. Build only what the unit's issue asks for. If the unit is unclear or depends on an unmerged unit, stop and ask the owner.
3. Open the PR as a draft. Mark it ready only after the unit's **Done when** check passes. Each ready PR spends shared review budget.
4. Paste real evidence in the PR: test output, screenshots with fictional data, or the content itself. Never describe a result you did not run or see.
5. Never weaken, skip or delete a test to make a check pass.
6. Antigravity edits only design files (docs/design.md and the CSS tokens file) inside U14. Codex owns app code. Do not let two agents edit the same files at once.

## Data and clinical content

1. All demo data is fictional. Never add real patient names, numbers or records.
2. Never write medicine doses, times, symptoms or escalation advice from memory. Clinical wording comes from U04 and is signed off by the pharmacy lead in U10.
3. Never invent survey results, participant feedback, market numbers or citations. A number needs a source and date, or is labelled an assumption.
4. Keep one patient's data invisible to other patients and unassigned clinicians. Every new route checks the role and the assignment on the server.
5. Mark anything a person must verify with `NEEDS HUMAN` in the PR.

## Commands

```
flask --app app reset-demo
flask --app app run
python -B -m unittest -v
```

Commands apply once U01 has merged.
