import tempfile
import unittest
from pathlib import Path

from app import create_app


class CareBudTest(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = Path(folder.name) / "demo.sqlite"
        self.app = create_app(self.path)
        self.reset()

    def reset(self):
        result = self.app.test_cli_runner().invoke(args=["reset-demo"])
        self.assertEqual(result.exit_code, 0, result.output)

    def login(self, role, account):
        client = self.app.test_client()
        response = client.post("/sign-in/" + role, data={"username": account, "password": "CareBud-demo"})
        self.assertEqual(response.status_code, 302)
        for _ in range(2):
            page = client.get("/")
            self.assertIn(b"Sign out", page.data)
        return client

    def test_patient_access(self):
        patient = self.login("patient", "patient-a")
        self.assertEqual(patient.get("/api/patients/patient-a/plan").status_code, 200)
        self.assertEqual(patient.get("/api/patients/patient-b/plan").status_code, 403)
        self.assertEqual(patient.patch("/api/patients/patient-a/plan", json={"goal":"Invalid"}).status_code, 403)
        patient.post("/sign-out")
        self.assertEqual(patient.get("/api/patients/patient-a/plan").status_code, 401)

    def test_clinician_access_and_restart(self):
        url = "/api/patients/patient-a/plan"
        clinician = self.login("clinician", "clinician-a")
        self.assertEqual(clinician.patch(url, json={"goal":"Discuss the next visit"}).status_code, 200)
        other = self.login("clinician", "clinician-b")
        self.assertEqual(other.patch(url, json={"goal":"Wrong assignment"}).status_code, 403)
        self.app = create_app(self.path)
        patient = self.login("patient", "patient-a")
        self.assertEqual(patient.get(url).json["goal"], "Discuss the next visit")
        self.reset()
        self.assertEqual(patient.get(url).status_code, 401)
        self.assertNotEqual(self.login("patient", "patient-a").get(url).json["goal"], "Discuss the next visit")

    def test_role_and_input_validation(self):
        client = self.app.test_client()
        self.assertEqual(client.post("/sign-in/clinician", data={
            "username":"patient-a", "password":"CareBud-demo"}).status_code, 401)
        clinician = self.login("clinician", "clinician-a")
        self.assertEqual(clinician.patch("/api/patients/patient-a/plan", json={"goal":" "}).status_code, 400)
