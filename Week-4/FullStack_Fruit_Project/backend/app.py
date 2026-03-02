from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import uuid

app = Flask(__name__)
CORS(app)

tokens = {}

def db():
    conn = sqlite3.connect("fruit.db")
    conn.row_factory = sqlite3.Row
    return conn

with db() as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT UNIQUE, password TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, quantity REAL, price REAL, user_id INTEGER)")

def auth_user():
    token = request.headers.get("Authorization")
    return tokens.get(token)

@app.route("/")
def home():
    return "Backend Running"

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = db()
    try:
        conn.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)",
                     (data["username"], data["email"], data["password"]))
        conn.commit()
        conn.close()
        return jsonify({"message": "Registered"})
    except:
        conn.close()
        return jsonify({"error": "Email already exists"}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = db()
    user = conn.execute("SELECT * FROM users WHERE email=? AND password=?",
                        (data["email"], data["password"])).fetchone()
    conn.close()
    if user:
        token = str(uuid.uuid4())
        tokens[token] = user["id"]
        return jsonify({"token": token, "username": user["username"]})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/fruits", methods=["GET"])
def get_fruits():
    user_id = auth_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    conn = db()
    fruits = conn.execute("SELECT * FROM fruits WHERE user_id=?", (user_id,)).fetchall()
    conn.close()
    return jsonify([dict(f) for f in fruits])

@app.route("/add", methods=["POST"])
def add_fruit():
    user_id = auth_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    conn = db()
    conn.execute("INSERT INTO fruits (name,quantity,price,user_id) VALUES (?,?,?,?)",
                 (data["name"], data["quantity"], data["price"], user_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Added"})

@app.route("/update/<int:id>", methods=["PUT"])
def update_fruit(id):
    user_id = auth_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    conn = db()
    conn.execute("UPDATE fruits SET name=?, quantity=?, price=? WHERE id=? AND user_id=?",
                 (data["name"], data["quantity"], data["price"], id, user_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Updated"})

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_fruit(id):
    user_id = auth_user()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    conn = db()
    conn.execute("DELETE FROM fruits WHERE id=? AND user_id=?", (id, user_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})