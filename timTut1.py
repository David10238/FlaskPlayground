
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page<h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name} git is synched with VSCode"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)