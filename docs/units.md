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
