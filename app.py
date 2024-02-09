from flask import Flask, render_template
import os

app = Flask(__name__)

# app routing


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


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5500")),
        debug=True,
    )
