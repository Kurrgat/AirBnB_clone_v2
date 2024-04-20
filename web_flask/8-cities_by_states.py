#!/usr/bin/python3
"""
Starting my first Flask web application
"""
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
