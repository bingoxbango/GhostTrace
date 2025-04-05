from flask import Flask, render_template, request, redirect, url_for, session
from app.ghosttrace_chat import chat_with_llm
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "ghosttrace"

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["user"] = USERNAME
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route('/chat', methods=["POST"])
def chat():
    user_input = request.form["prompt"]
    response = chat_with_llm(user_input)
    return response
