#!/usr/bin/python3
''' update some part of our engine:'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states_list.html', states=sorted_states)

@app.teardown_appcontext
def close_session(exception=None):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
