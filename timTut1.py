
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/") # home route
def home():
    return "Welcome to the home page<h1>HELLO<h1>"

@app.route("/<name>") # passing parameter to method
def user(name):
    return f"Hello {name} git is synched with VSCode"

@app.route("/admin/") # / at end allows having / at end
def admin():
    return redirect(url_for("user", name="Admin")) #redirecting to another function

if __name__ == "__main__":
    app.run(debug=True)