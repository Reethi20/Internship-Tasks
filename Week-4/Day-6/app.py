from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = connect_db()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY AUTOINCREMENT, fruit_name TEXT NOT NULL, quantity_kg REAL NOT NULL, price_per_kg REAL NOT NULL)"
    )
    conn.commit()
    conn.close()

create_table()

@app.route("/")
def home():
    conn = connect_db()
    fruits = conn.execute("SELECT * FROM fruits").fetchall()
    conn.close()
    return render_template("home.html", fruits=fruits)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        fruit_name = request.form["fruit_name"]
        quantity_kg = request.form["quantity_kg"]
        price_per_kg = request.form["price_per_kg"]
        conn = connect_db()
        conn.execute(
            "INSERT INTO fruits (fruit_name, quantity_kg, price_per_kg) VALUES (?, ?, ?)",
            (fruit_name, quantity_kg, price_per_kg),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    conn = connect_db()
    fruit = conn.execute("SELECT * FROM fruits WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        fruit_name = request.form["fruit_name"]
        quantity_kg = request.form["quantity_kg"]
        price_per_kg = request.form["price_per_kg"]
        conn.execute(
            "UPDATE fruits SET fruit_name = ?, quantity_kg = ?, price_per_kg = ? WHERE id = ?",
            (fruit_name, quantity_kg, price_per_kg, id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("home"))

    conn.close()
    return render_template("update.html", fruit=fruit)

@app.route("/delete/<int:id>")
def delete(id):
    conn = connect_db()
    conn.execute("DELETE FROM fruits WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)