#!/usr/bin/python3
"""A script that starts a Flask web application:
listening on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """Starts a Flask application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Starts a Flask application"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def after_text():
    """Starts a Flask application"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/c/python/<text>', strict_slashes=False)
def after_python_text():
    """Starts a Flask application"""
    text = text.replace('_', ' ')
    return 'Python is {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
