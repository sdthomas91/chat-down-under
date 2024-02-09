# IMPORTS
import os
from auth import auth
from flask import Flask, render_template, request, flash

# Flask app instance
app = Flask(__name__)


# MAIN NAV ROUTES


@app.route("/")
def index():
    """
    Return the home page displaying latest questions and profile dashboard
    if logged in
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Navigate to the about page
    """
    return render_template("about.html")


@app.route("/topics")
def topics():
    """
    Navigate to the topics page
    """
    return render_template("topics.html")


# LOGIN/LOGOUT/SIGNUP


@app.route("/signup")
def signup():
    """
    Navigate to the signup page
    """
    return render_template("signup.html")


@app.route("/login")
def login():
    """
    Navigate to the login page
    """
    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Navigate to the logout page
    """
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5500")),
        debug=True,
    )
