# CareBud

CareBud is a hackathon prototype for the time between clinic visits. A clinician publishes a plan, a patient sees what to do today, and both can use the patient's symptom notes at follow-up. Demo accounts use fictional data.

## Start here

[Open the unit issues](https://github.com/aly570/CareBud/issues) or read the [unit plan and acceptance checks](docs/units.md). Start with the first unit in your row. The owner implements the unit and collects evidence for its check.

| Owner | Start now | Later |
| --- | --- | --- |
| CS 1 · integration | U01 · sign-in, permissions and shared data contract | U09 · QR sharing, U12 · release |
| CS 2 · clinician tools | U02 · care-plan editor | U06 · publication, U08 · diary and follow-up |
| CS 3 · patient app | U03 · daily plan | U07 · reminders and progress |
| Mechanical engineering · human factors | U05 · patient journey and test design | U11 · usability testing and demo |
| Pharmacy · clinical content | U04 · fictional care plan | U10 · clinical walkthrough |

## Working agreement

1. Start a branch for one unit, for example `u03-patient-plan`. Use a draft PR while building. Include the unit ID in the title and link the issue with `Closes #NUMBER`.
2. Run the check in the issue and attach its evidence. Sketches, a test sheet and a clinical content review can each be the deliverable for a PR.
3. Mark the PR ready when its dependencies have merged and its check passes. Claude reviews the current change. If it finds a blocker, fix it on the same branch. Use draft mode while making several fixes together.
4. A teammate checks the Claude verdict for the latest commit and the unit evidence, then merges. An unavailable review or a request for changes keeps the unit open. Start independent units in parallel.

Codex owns planning, implementation support and fixes. Claude Code owns independent review. The pharmacy lead checks clinical wording. See [review setup](docs/review.md). The first milestone is a mobile-friendly, fictional-data demo. A guideline-search assistant and hospital integration can be scoped after that demo.
