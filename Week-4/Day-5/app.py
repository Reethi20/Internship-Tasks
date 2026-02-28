from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret"
db = "users.db"

def init_db():
    if not os.path.exists(db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)")
        con.commit()
        con.close()

def add_user(e, p):
    con = sqlite3.connect(db)
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO users(email,password) VALUES(?,?)", (e, p))
        con.commit()
        con.close()
        return True
    except:
        con.close()
        return False

def check_user(e, p):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE email=? AND password=?", (e, p))
    user = cur.fetchone()
    con.close()
    return user

@app.route("/", methods=["GET", "POST"])
def signup():
    msg = ""
    if request.method == "POST":
        e = request.form["email"]
        p = request.form["password"]
        if add_user(e, p):
            return redirect(url_for("signin"))
        else:
            msg = "Email already exists"
    return render_template("signup.html", msg=msg)

@app.route("/signin", methods=["GET", "POST"])
def signin():
    msg = ""
    if request.method == "POST":
        e = request.form["email"]
        p = request.form["password"]
        if check_user(e, p):
            session["user"] = e
            return redirect(url_for("home"))
        else:
            msg = "Invalid credentials"
    return render_template("signin.html", msg=msg)

@app.route("/home")
def home():
    if "user" in session:
        return render_template("home.html", email=session["user"])
    return redirect(url_for("signin"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("signin"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)