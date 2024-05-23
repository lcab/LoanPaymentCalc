from flask import Flask, render_template, url_for

#import requests
#import json
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/")
def layout():
    return render_template("layout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)