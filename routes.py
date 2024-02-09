from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)


""" 
Setup for routes file as separate inspired by youtube Tech with Tim url - youtube.com/watch?v=dam0GPOAvVI
"""
# MAIN NAV ROUTES


@routes.route("/")
def index():
    """
    Return the home page displaying latest questions and profile dashboard
    if logged in
    """
    return render_template("index.html", page_title="Welcome to Chat Down Under")


@routes.route("/about")
def about():
    """
    Navigate to the about page
    """
    return render_template("about.html", page_title="About Our Forum")


@routes.route("/topics")
def topics():
    """
    Navigate to the topics page
    """
    return render_template("topics.html", page_title="Browse by Topic")


# LOGIN/LOGOUT/SIGNUP


@routes.route("/signup")
def signup():
    """
    Navigate to the signup page
    """
    return render_template("signup.html", page_title="Register for an Account")


@routes.route("/login")
def login():
    """
    Navigate to the login page
    """
    return render_template("login.html", page_title="Login to Your Account")


@routes.route("/logout")
def logout():
    """
    Navigate to the logout page
    """
    return render_template("logout.html", page_title="Logout Successful")
