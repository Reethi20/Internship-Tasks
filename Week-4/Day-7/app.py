from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "fruitshop"

def db():
    conn = sqlite3.connect("fruit.db")
    conn.row_factory = sqlite3.Row
    return conn

with db() as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT UNIQUE, password TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY AUTOINCREMENT, fruit_name TEXT, quantity REAL, price REAL, user_id INTEGER)")

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if request.method == "POST":
        u, e, p = request.form["username"], request.form["email"], request.form["password"]
        conn = db()
        if conn.execute("SELECT 1 FROM users WHERE email=?", (e,)).fetchone():
            msg = "Email already registered"
        else:
            conn.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)", (u,e,p))
            conn.commit()
            conn.close()
            return redirect("/login")
        conn.close()
    return render_template("register.html", message=msg)

@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        e, p = request.form["email"], request.form["password"]
        conn = db()
        user = conn.execute("SELECT * FROM users WHERE email=?", (e,)).fetchone()
        conn.close()
        if user and user["password"] == p:
            session["uid"], session["name"] = user["id"], user["username"]
            return redirect("/dashboard")
        msg = "Invalid credentials"
    return render_template("login.html", message=msg)

@app.route("/dashboard")
def dashboard():
    if "uid" not in session:
        return redirect("/login")
    conn = db()
    fruits = conn.execute("SELECT * FROM fruits WHERE user_id=?", (session["uid"],)).fetchall()
    conn.close()
    return render_template("dashboard.html", fruits=fruits, username=session["name"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if "uid" not in session:
        return redirect("/login")
    if request.method == "POST":
        f, q, pr = request.form["fruit_name"], request.form["quantity_kg"], request.form["price_per_kg"]
        conn = db()
        conn.execute("INSERT INTO fruits (fruit_name,quantity,price,user_id) VALUES (?,?,?,?)", (f,q,pr,session["uid"]))
        conn.commit()
        conn.close()
        return redirect("/dashboard")
    return render_template("add_fruit.html")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if "uid" not in session:
        return redirect("/login")
    conn = db()
    if request.method == "POST":
        f, q, pr = request.form["fruit_name"], request.form["quantity_kg"], request.form["price_per_kg"]
        conn.execute("UPDATE fruits SET fruit_name=?, quantity=?, price=? WHERE id=? AND user_id=?", (f,q,pr,id,session["uid"]))
        conn.commit()
        conn.close()
        return redirect("/dashboard")
    fruit = conn.execute("SELECT * FROM fruits WHERE id=? AND user_id=?", (id,session["uid"])).fetchone()
    conn.close()
    return render_template("update_fruit.html", fruit=fruit)

@app.route("/delete/<int:id>")
def delete(id):
    if "uid" in session:
        conn = db()
        conn.execute("DELETE FROM fruits WHERE id=? AND user_id=?", (id,session["uid"]))
        conn.commit()
        conn.close()
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)