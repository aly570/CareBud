# Unit 1 app contract

The demo is a mobile-friendly web app running on localhost. Python 3.13, Flask and SQLite. All four demo accounts use the password `CareBud-demo`. Clinician A is assigned patient A, clinician B is assigned patient B. Account names use lowercase, for example `patient-b`.

## Windows quick start

From the repo folder run these in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m flask --app app reset-demo
.\.venv\Scripts\python -m flask --app app run
```

Open http://127.0.0.1:5000 and choose Patient or Clinician. Reset replaces the fictional records and revokes existing sessions. Run the unit checks with `.\.venv\Scripts\python -m unittest -v`. They use an isolated temporary database.

## Integration

Use the same origin and the session cookie set by sign-in. GET /api/patients/{patient}/plan returns this shape. The entry shapes shown are the contract for upcoming UI units. The initial seed has empty lists.

```json
{
  "goal": "Prepare one question for the next visit",
  "medications": [{"name": "Fictional medicine", "instructions": "Demo instructions", "times": ["09:00"]}],
  "visits": [{"startsAt": "2026-12-01T09:00:00+03:00", "label": "Fictional follow-up"}],
  "diary": [{"recordedAt": "2026-11-22T08:00:00+03:00", "note": "Fictional note", "severity": 2}]
}
```

Medication times are local Qatar wall times. Visit and diary timestamps include the offset. Severity may be null or an integer from 0 through 10. PATCH on the same URL accepts exactly one field, `goal`, a trimmed nonempty string of at most 300 characters, and returns the updated plan. Only the assigned clinician can patch. Patients can read their own plan. Missing sessions return 401 and access outside the assignment returns 403. This demo endpoint supports the U01 access check; U06 adds draft and publication semantics.
