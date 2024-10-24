#!/usr/bin/env python3
"""
Exercise 2: Use the 'babel.localeselector'
to find the best matching available language
to give to the user.
"""
import flask
import flask_babel
from typing import Optional
from os import environ


class Config:
    """
    Configuration class for Babel and allowed languages.
    Contains the allowed languages and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = flask.Flask(__name__)
app.config.from_object(Config)
babel = flask_babel.Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Select the best match for supported languages from the request.
    """
    return flask.request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def home() -> str:
    """
    Render the home page template with localized content.
    """
    return flask.render_template("2-index.html")


if __name__ == "__main__":
    # Fallback to '0.0.0.0' and port 5000 if no HOST/PORT env vars are defined
    host = environ.get("HOST", "0.0.0.0")
    port = int(environ.get("PORT", 5000))
    app.run(host=host, port=port)
