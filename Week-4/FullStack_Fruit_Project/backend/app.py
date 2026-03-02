from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import uuid

app = Flask(__name__)
CORS(app)

tokens = {}

def connect():
    conn = sqlite3.connect("fruit.db")
    conn.row_factory = sqlite3.Row
    return conn

with connect() as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT UNIQUE, password TEXT, role TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, quantity REAL, owner_id INTEGER)")
    conn.execute("CREATE TABLE IF NOT EXISTS basket (id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id INTEGER, fruit_id INTEGER, quantity REAL)")

def get_user():
    token = request.headers.get("Authorization")
    if token in tokens:
        return tokens[token]
    return None

@app.route("/")
def home():
    return "Backend Running"

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = connect()
    try:
        conn.execute("INSERT INTO users (username,email,password,role) VALUES (?,?,?,?)",
                     (data["username"], data["email"], data["password"], data["role"]))
        conn.commit()
        conn.close()
        return jsonify({"message": "Registered"})
    except:
        conn.close()
        return jsonify({"error": "Email already exists"}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = connect()
    user = conn.execute("SELECT * FROM users WHERE email=? AND password=?",
                        (data["email"], data["password"])).fetchone()
    conn.close()

    if user:
        token = str(uuid.uuid4())
        tokens[token] = {"id": user["id"], "role": user["role"], "username": user["username"]}
        return jsonify({"token": token, "role": user["role"], "username": user["username"]})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/fruits", methods=["GET"])
def get_fruits():
    conn = connect()
    fruits = conn.execute("SELECT fruits.*, users.username as owner FROM fruits JOIN users ON fruits.owner_id = users.id").fetchall()
    conn.close()
    return jsonify([dict(f) for f in fruits])

@app.route("/add_fruit", methods=["POST"])
def add_fruit():
    user = get_user()
    if not user or user["role"] != "owner":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    conn = connect()
    conn.execute("INSERT INTO fruits (name,price,quantity,owner_id) VALUES (?,?,?,?)",
                 (data["name"], data["price"], data["quantity"], user["id"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Fruit added"})

@app.route("/update_fruit/<int:id>", methods=["PUT"])
def update_fruit(id):
    user = get_user()
    if not user or user["role"] != "owner":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    conn = connect()
    conn.execute("UPDATE fruits SET name=?, price=?, quantity=? WHERE id=? AND owner_id=?",
                 (data["name"], data["price"], data["quantity"], id, user["id"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Updated"})

@app.route("/delete_fruit/<int:id>", methods=["DELETE"])
def delete_fruit(id):
    user = get_user()
    if not user or user["role"] != "owner":
        return jsonify({"error": "Unauthorized"}), 401

    conn = connect()
    conn.execute("DELETE FROM fruits WHERE id=? AND owner_id=?", (id, user["id"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})

@app.route("/add_to_basket", methods=["POST"])
def add_to_basket():
    user = get_user()
    if not user or user["role"] != "customer":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    conn = connect()
    conn.execute("INSERT INTO basket (customer_id,fruit_id,quantity) VALUES (?,?,?)",
                 (user["id"], data["fruit_id"], data["quantity"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Added to basket"})

@app.route("/view_basket", methods=["GET"])
def view_basket():
    user = get_user()
    if not user or user["role"] != "customer":
        return jsonify({"error": "Unauthorized"}), 401

    conn = connect()
    items = conn.execute("""
        SELECT basket.id, fruits.name, fruits.price, basket.quantity 
        FROM basket 
        JOIN fruits ON basket.fruit_id = fruits.id
        WHERE basket.customer_id=?
    """, (user["id"],)).fetchall()

    total = 0
    result = []
    for item in items:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        result.append({
            "id": item["id"],
            "name": item["name"],
            "price": item["price"],
            "quantity": item["quantity"],
            "subtotal": subtotal
        })

    conn.close()
    return jsonify({"items": result, "total": total})

@app.route("/remove_from_basket/<int:id>", methods=["DELETE"])
def remove_from_basket(id):
    user = get_user()
    if not user or user["role"] != "customer":
        return jsonify({"error": "Unauthorized"}), 401

    conn = connect()
    conn.execute("DELETE FROM basket WHERE id=? AND customer_id=?", (id, user["id"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Removed"})