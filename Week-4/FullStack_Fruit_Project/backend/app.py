from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def db():
    conn = sqlite3.connect("fruit.db")
    conn.row_factory = sqlite3.Row
    return conn

with db() as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, quantity REAL, price REAL)")

@app.route("/")
def home():
    return "Fruit Shop Backend Running"

@app.route("/fruits", methods=["GET"])
def get_fruits():
    conn = db()
    fruits = conn.execute("SELECT * FROM fruits").fetchall()
    conn.close()
    return jsonify([dict(f) for f in fruits])

@app.route("/add", methods=["POST"])
def add_fruit():
    data = request.json
    conn = db()
    conn.execute("INSERT INTO fruits (name, quantity, price) VALUES (?, ?, ?)",
                 (data["name"], data["quantity"], data["price"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Added"})

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_fruit(id):
    conn = db()
    conn.execute("DELETE FROM fruits WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run()