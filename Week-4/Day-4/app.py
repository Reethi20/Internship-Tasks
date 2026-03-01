from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("event.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        event TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    event = request.form["event"]

    conn = sqlite3.connect("event.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO registrations (name, email, event) VALUES (?, ?, ?)",
        (name, email, event)
    )
    conn.commit()
    conn.close()

    return redirect("/registrations")

@app.route("/registrations")
def registrations():
    conn = sqlite3.connect("event.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registrations")
    data = cursor.fetchall()
    conn.close()

    return render_template("display.html", records=data)

import os

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)