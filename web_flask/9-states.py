#!/usr/bin/python3
'''Starts a Flask web app listening on 0.0.0.0 port 5000'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(execption):
    '''starts a Flask web application'''
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    '''starts a Flask web application'''
    list_state = storage.all(State).values()
    return render_template('7-states_list.html', list=list_state)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    '''starts a Flask web application'''
    list_state = storage.all(State).values()
    for element in list_state:
        if element.id == id:
            return render_template('9-states.html', state=element,
                                   list=list_state, id=1)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
