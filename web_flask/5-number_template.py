#!/usr/bin/python3
"""A script that starts a Flask web application:
listening on 0.0.0.0, port 5000"""
from flask import Flask, render_template

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
def after_text(text):
    """Starts a Flask application"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def after_python_text(text='is cool'):
    """Starts a Flask application"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Starts a Flask application"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def show_template(n):
    """Starts a Flask application"""
    return render_template('5-number.html', num=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
