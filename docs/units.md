# CareBud work units

Five lanes start independently. U02 and U03 use fictional fixtures while U01 defines the integration contract. Coordinate field names on day one. A unit is complete when its check passes and the PR is merged. The team may change proposed scope in the issue before implementation.

## U01 · Demo app and access rules

**Owner** CS 1  
**Depends on** None. Ready to start.

Create the mobile-friendly app shell, persistent demo database and repeatable seed/reset. Provide separate clinician and patient sign-in entry points, server-side roles and patient-to-clinician assignments. Publish a small data contract for plans, medication times, visits and diary entries so both UI owners can integrate.

**Done when**  
Start from a clean checkout. Sign in as each role, reload successfully, then show that one patient cannot fetch another patient's plan and an unassigned clinician cannot edit it.

## U02 · Clinician care-plan editor

**Owner** CS 2  
**Depends on** None. Ready to start.

Build the clinician flow against a fictional fixture. Include problems, goals, medicine instructions and times, appointments, signs of improvement, and instructions for concerning symptoms. Keep draft and published states visibly distinct.

**Done when**  
A clinician can add and edit each field, correct an invalid time and preview the published version. Capture the flow or a component test.

## U03 · Patient daily plan

**Owner** CS 3  
**Depends on** None. Ready to start.

Build a mobile patient view using a fictional fixture. Show today's tasks in time order, the next visit, the clinician's instructions, and where to find goals and signs to watch for.

**Done when**  
On a phone-sized screen, find the next medicine and appointment, locate the clinician's instructions and distinguish an empty day from a loading error.

## U04 · Fictional care plan and clinical wording

**Owner** Pharmacy  
**Depends on** None. Ready to start.

Write one fictional care-plan example in plain Arabic, with goals, medication schedule, a follow-up, expected improvement and clinician-authored escalation instructions. Record the source and date for each clinical claim. Mark items needing professional verification.

**Done when**  
Deliver one versioned example and a source table. A teammate can identify the next action and when to contact the care team using the example alone.

## U05 · Patient journey and usability test design

**Owner** Mechanical engineering  
**Depends on** None. Ready to start.

Map the handoffs from clinic visit to medicine reminder, symptom entry and follow-up. Sketch the screens and design a short phone-based usability test with success criteria. Use the existing survey as input when available.

**Done when**  
Deliver a flow diagram or sketches and a test sheet for finding a dose time, recording pain and finding the next appointment. Record how task completion and mistakes will be counted.

## U06 · Publish the plan to the correct patient

**Owner** CS 2  
**Depends on** U01, U02, U04

Connect the clinician editor to persistent storage, seed the pharmacy example and expose the latest published version to its assigned patient. Keep edits to a new draft separate until publication.

**Done when**  
Publish a plan, change a dose time in a draft and reload as the patient. Only a second publish changes what that patient sees. An unrelated patient is denied.

## U07 · Reminders and daily progress

**Owner** CS 3  
**Depends on** U01, U03, U06

Read the latest published plan. Schedule medicine and visit reminders in the supported demo environment, show notification permission status and an in-app fallback, and acknowledge completed tasks with encouraging language.

**Done when**  
On the stated device deliver one test reminder, handle denied notifications, complete a task twice without double credit, reload, and change a medicine time without leaving a stale reminder. Document when the app must be open.

## U08 · Symptom diary and clinician follow-up

**Owner** CS 2  
**Depends on** U01, U03, U06

Let the patient record pain or another symptom with time, an optional severity and a note. Show a chronological diary to the assigned clinician and allow a follow-up message visible to the patient.

**Done when**  
Record two distinct times, reload and confirm both appear in order for the assigned clinician. Reply from the clinician account and verify receipt and isolation from the second patient.

## U09 · Patient-controlled QR summary

**Owner** CS 1  
**Depends on** U01, U06

Add a patient preview of the exact fields to share, explicit consent, a short-lived opaque link, a scannable QR code and revocation. Exclude private notes and clinician messages.

**Done when**  
Scan the QR on a second device. Match the preview, inspect the QR payload for personal details, revoke it and verify access stops. Repeat with an expired link.

## U10 · Review the clinical demo

**Owner** Pharmacy  
**Depends on** U04, U06

Walk the fictional case through both roles. Check medicine wording and times, expected improvement, escalation instructions and Arabic readability. Record observed issues and sign off on the corrected demo wording.

**Done when**  
Compare each published field against U04. Record reviewer, date and disposition of discrepancies. Escalate unresolved clinical wording to a qualified clinician before any real-world use.

## U11 · Test the prototype and prepare the live demo

**Owner** Mechanical engineering  
**Depends on** U05, U07, U08, U09

Run the U05 tasks with volunteers using fictional accounts. Record anonymous observations, device, task completion and confusion. Rehearse the clinician-to-patient handoff and QR scan. Prepare a short presentation script.

**Done when**  
Report actual participant and task counts alongside observed failures. Link fixes or limitations. A second teammate can reproduce the demo from the script.

## U12 · End-to-end release rehearsal

**Owner** CS 1  
**Depends on** U07, U08, U09, U10, U11

Integrate the five workstreams, run the two-account demo from a clean seed, verify overnight/timezone assumptions and write the release notes and demo startup instructions.

**Done when**  
A teammate follows the README on a clean checkout and completes publish → reminder → diary → clinician reply → QR revocation. Attach check output and remaining limitations.

## Submission, hosting and design units

These units cover the hackathon deliverables: demo link, pitch deck, team profile, market rationale, implementation plan, the two 100-word statements and the AI tools disclosure. Content units are reviewed like code: paste the actual document, counts or test results in the PR.

## U13 · Host the public demo link

**Owner** CS 3  
**Issue** #14  
**Depends on** U01 (#1)

Deploy the Flask demo to a free host with HTTPS so judges and testers can open it on a phone. Document the host, the seed/reset command and how to redeploy after a merge. Keep demo data fictional.

**Done when**  
A teammate opens the HTTPS link on a phone using mobile data, signs in with a demo account, and reloads. Reset the demo with the one documented command. Confirm the browser can show the notification permission prompt that U07 (#7) needs.

## U14 · Visual design and UI style

**Owner** CS 3, with Mechanical engineering input  
**Issue** #15  
**Depends on** U05 (#5) sketches when available

Use Antigravity to design the look of the patient day view and the clinician editor. Deliver docs/design.md and one CSS tokens file (colours, type sizes, spacing, right-to-left rules for Arabic). Antigravity changes only these design files in this unit, so it does not collide with Codex work on app code.

**Done when**  
Mockups of both screens are in the PR. Text contrast meets WCAG AA, tap targets are at least 44 px, and an Arabic sample renders right-to-left. The tokens file is linked from README.

## U15 · Problem and solution statements and team profile

**Owner** Pharmacy (statements), Mechanical engineering (team profile)  
**Issue** #16  
**Depends on** None. Ready to start.

Write the hackathon problem statement and solution statement in simple English, and the team profile with each member's major and role. Save them in docs/submission.md.

**Done when**  
Each statement is 100 words or fewer, with the word count shown. Every claim about patients, demand or outcomes has a cited source and date, or is marked as a hypothesis. The team profile lists all five members and their units.

## U16 · Market rationale and implementation plan

**Owner** Pharmacy (market), CS 1 (technical plan)  
**Issue** #17  
**Depends on** U15 (#16)

Write the market rationale (target users, Qatar care context, alternatives, cost and who pays) and the implementation plan (what the prototype does, what real use would need: clinical sign-off, data protection, hospital integration, timeline). Save them in docs/market-and-plan.md.

**Done when**  
Every number has a source and date or is labelled an assumption. The plan separates what is built from what is proposed. A teammate can answer "who pays and why" and "what happens before real patients use it" from the doc alone.

## U17 · Pitch deck and pitch script

**Owner** Mechanical engineering  
**Issue** #18  
**Depends on** U15 (#16), U16 (#17), U11 (#11)

Build the pitch deck: problem, solution, live demo, evidence (survey and usability results), market, implementation plan, team. Write a timed script that matches the U11 (#11) demo script.

**Done when**  
Attach the deck and the timed rehearsal result within the event's time limit. A second teammate can present from the script. Every result shown matches the actual counts in U11 (#11) or U18 (#19).

## U18 · Launch the survey and analyse responses

**Owner** Mechanical engineering  
**Issue** #19  
**Depends on** None. Ready to start.

Send the existing survey (CareBud-Survey.gs) to real respondents with a consent line and no identifying questions. Summarise the responses for the deck and for U05 (#5).

**Done when**  
Report the actual number of responses and the date range, with a chart or table of the main answers. No invented or mock numbers. If responses are too few to support a claim, the summary says so.

## U19 · AI tools disclosure and demo safety notes

**Owner** CS 1  
**Issue** #20  
**Depends on** None. Ready to start.

State in README and docs/submission.md which third-party AI tools were used and for what (Codex for planning and code, Claude Code for PR review, Antigravity for UI design), that all demo data is fictional, and that clinical content needs professional sign-off before any real use.

**Done when**  
A reader of README can name each AI tool and its role. The disclosure matches the event rules if they ask for one. The fictional-data and clinical sign-off notes appear on the demo sign-in page.
