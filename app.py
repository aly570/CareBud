"""CareBud local demo. Start with flask --app app reset-demo, then flask run."""
import hashlib
import json
import secrets
import sqlite3
import time
from pathlib import Path

from flask import Flask, abort, g, jsonify, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash


def create_app(database=None):
    app = Flask(__name__)
    app.config["DATABASE"] = Path(database or Path(app.instance_path) / "demo.sqlite")

    def db():
        if "db" not in g:
            path = app.config["DATABASE"]
            path.parent.mkdir(parents=True, exist_ok=True)
            g.db = sqlite3.connect(path)
            g.db.row_factory = sqlite3.Row
            g.db.execute("PRAGMA foreign_keys = ON")
        return g.db

    @app.teardown_appcontext
    def close_db(error):
        if "db" in g:
            g.db.close()

    @app.cli.command("reset-demo")
    def reset_demo():
        conn = db()
        password = generate_password_hash("CareBud-demo")
        conn.executescript("""
            BEGIN IMMEDIATE;
            DROP TABLE IF EXISTS sessions;
            DROP TABLE IF EXISTS plans;
            DROP TABLE IF EXISTS users;
            CREATE TABLE users(id TEXT PRIMARY KEY, name TEXT NOT NULL, role TEXT NOT NULL,
                password TEXT NOT NULL, clinician TEXT REFERENCES users(id));
            CREATE TABLE plans(patient TEXT PRIMARY KEY REFERENCES users(id), body TEXT NOT NULL);
            CREATE TABLE sessions(token TEXT PRIMARY KEY, user TEXT REFERENCES users(id), expires INTEGER);
        """)
        for clinician, patient, name, clinician_name in [
            ("clinician-a", "patient-a", "Noor", "Dr. Samir"),
            ("clinician-b", "patient-b", "Omar", "Dr. Dana"),
        ]:
            conn.execute("INSERT INTO users VALUES(?,?,?,?,NULL)",
                         (clinician, clinician_name, "clinician", password))
            conn.execute("INSERT INTO users VALUES(?,?,?,?,?)",
                         (patient, name, "patient", password, clinician))
            plan = dict(goal="Prepare one question for the next visit", medications=[],
                        visits=[], diary=[])
            conn.execute("INSERT INTO plans VALUES(?,?)", (patient, json.dumps(plan)))
        conn.commit()
        print("Fictional accounts and plans are ready.")

    def token_hash(token):
        return hashlib.sha256(token.encode()).hexdigest()

    @app.before_request
    def load_user():
        if request.method not in ("GET", "HEAD", "OPTIONS"):
            origin = request.headers.get("Origin")
            if origin and origin != request.host_url.rstrip("/"):
                abort(403)
        cookie = request.cookies.get("carebud_session")
        g.user = None
        if cookie:
            g.user = db().execute("""
                SELECT users.* FROM sessions JOIN users ON sessions.user = users.id
                WHERE token = ? AND expires > ?
            """, (token_hash(cookie), time.time())).fetchone()

    @app.after_request
    def private_pages(response):
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.get("/")
    def home():
        if not g.user:
            return render_template("home.html")
        if g.user["role"] == "patient":
            people = [g.user]
        else:
            people = db().execute("SELECT * FROM users WHERE clinician=? ORDER BY name",
                                  (g.user["id"],)).fetchall()
        cards = [(p["name"], read_plan(p["id"])) for p in people]
        return render_template("workspace.html", cards=cards)

    @app.route("/sign-in/<role>", methods=["GET", "POST"])
    def login(role):
        if role not in {"patient", "clinician"}:
            abort(404)
        if request.method == "GET":
            return render_template("login.html", role=role)
        user = db().execute("SELECT * FROM users WHERE id=? AND role=?",
                            (request.form.get("username"), role)).fetchone()
        if not user or not check_password_hash(user["password"], request.form.get("password", "")):
            return render_template("login.html", role=role, error="Check your account and password."), 401
        token = secrets.token_urlsafe(32)
        with db():
            db().execute("DELETE FROM sessions WHERE token=? OR expires<=?",
                         (token_hash(request.cookies.get("carebud_session", "")), time.time()))
            db().execute("INSERT INTO sessions VALUES(?,?,?)",
                         (token_hash(token), user["id"], int(time.time()) + 28800))
        response = redirect(url_for("home"))
        response.set_cookie("carebud_session", token, httponly=True, samesite="Strict",
                            secure=request.is_secure, max_age=28800)
        return response

    @app.post("/sign-out")
    def logout():
        with db():
            db().execute("DELETE FROM sessions WHERE token=?",
                         (token_hash(request.cookies.get("carebud_session", "")),))
        response = redirect(url_for("home"))
        response.delete_cookie("carebud_session")
        return response

    def read_plan(patient):
        row = db().execute("SELECT body FROM plans WHERE patient=?", (patient,)).fetchone()
        return json.loads(row["body"])

    @app.route("/api/patients/<patient>/plan", methods=["GET", "PATCH"])
    def plan(patient):
        if not g.user:
            abort(401)
        assigned = db().execute("SELECT clinician FROM users WHERE id=? AND role='patient'",
                                (patient,)).fetchone()
        can_edit = assigned and assigned["clinician"] == g.user["id"] and g.user["role"] == "clinician"
        if not can_edit and (request.method == "PATCH" or g.user["id"] != patient):
            abort(403)
        if request.method == "PATCH":
            data = request.get_json()
            if not isinstance(data, dict) or set(data) != {"goal"} or not isinstance(data["goal"], str):
                abort(400)
            goal = data["goal"].strip()
            if not 1 <= len(goal) <= 300:
                abort(400)
            with db():
                db().execute("UPDATE plans SET body=json_set(body, '$.goal', ?) WHERE patient=?",
                             (goal, patient))
        return jsonify(read_plan(patient))

    return app
