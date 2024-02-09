# IMPORTS
import os
from auth import auth
from routes import routes
from flask import Flask, render_template, request, flash

# Flask app instance
app = Flask(__name__)

# register blueprints
app.register_blueprint(routes, url_prefix="/")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5500")),
        debug=True,
    )
