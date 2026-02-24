from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!! This is the home page of our Flask application."

if __name__ == "__main__":
    app.run(debug=True)