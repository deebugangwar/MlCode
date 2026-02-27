from flask import Flask, render_template, request, jsonify, session
import sqlite3
import random
import time
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey123"

DATABASE = "users.db"

# ================= DATABASE INIT =================

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    users = [
        ("A101", "Deebu", generate_password_hash("1234"), "admin"),
        ("T101", "Rahul", generate_password_hash("1234"), "teacher"),
        ("S101", "Aman", generate_password_hash("1234"), "student")
    ]

    for user in users:
        cursor.execute("INSERT OR IGNORE INTO users VALUES (?,?,?,?)", user)

    conn.commit()
    conn.close()

# ================= HOME =================

@app.route("/")
def home():
    return render_template("login.html")

# ================= LOGIN =================

@app.route("/login", methods=["POST"])
def login():

    user_id = request.form["id"]
    name = request.form["name"]
    password = request.form["password"]

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT password, role FROM users WHERE id=? AND name=?", (user_id, name))
    result = cursor.fetchone()

    conn.close()

    if result:
        stored_password, role = result

        if check_password_hash(stored_password, password):

            session["user"] = name
            session["role"] = role

            if role == "admin":
                return jsonify({"redirect": "/admin_dashboard"})
            elif role == "teacher":
                return jsonify({"redirect": "/teacher_dashboard"})
            elif role == "student":
                return jsonify({"redirect": "/student_dashboard"})

    return jsonify({"error": "Invalid ID, Name or Password"})

# ================= DASHBOARDS =================

@app.route("/admin_dashboard")
def admin_dashboard():
    if session.get("role") != "admin":
        return "Unauthorized Access"
    return "<h2>Welcome Admin</h2><a href='/logout'>Logout</a>"

@app.route("/teacher_dashboard")
def teacher_dashboard():
    if session.get("role") != "teacher":
        return "Unauthorized Access"
    return "<h2>Welcome Teacher</h2><a href='/logout'>Logout</a>"

@app.route("/student_dashboard")
def student_dashboard():
    if session.get("role") != "student":
        return "Unauthorized Access"
    return "<h2>Welcome Student</h2><a href='/logout'>Logout</a>"

# ================= LOGOUT =================

@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")

# ================= FORGOT PASSWORD PAGE =================

@app.route("/forgot_page")
def forgot_page():
    return render_template("forgot.html")

# ================= SEND OTP =================

@app.route("/send_otp", methods=["POST"])
def send_otp():

    contact = request.form["contact"]

    otp = str(random.randint(1000, 9999))

    session["otp"] = otp
    session["contact"] = contact
    session["otp_time"] = time.time()

    print("OTP is:", otp,flush=True)  # Terminal me dikhega

    return jsonify({"message": "OTP Sent Successfully"})

# ================= VERIFY OTP =================

@app.route("/verify_otp", methods=["POST"])
def verify_otp():

    entered_otp = request.form["otp"]

    if "otp_time" not in session:
        return jsonify({"status": "expired"})

    if time.time() - session["otp_time"] > 30:
        return jsonify({"status": "expired"})

    if session.get("otp") == entered_otp:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"})

# ================= RESET PASSWORD =================

@app.route("/reset_password", methods=["POST"])
def reset_password():

    new_password = request.form["new_password"]
    contact = session.get("contact")

    if not contact:
        return jsonify({"message": "Session Expired"})

    hashed_password = generate_password_hash(new_password)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET password=? WHERE name=?", (hashed_password, contact))

    conn.commit()
    conn.close()

    session.clear()

    return jsonify({"message": "Password Updated Successfully"})

# ================= RUN =================

if __name__ == "__main__":
    init_db()
    app.run(debug=True)