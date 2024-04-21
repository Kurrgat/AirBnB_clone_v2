#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Route that displays 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Route that displays 'C ', followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """Route that displays 'Python ', followed by the value of the text variable."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Route that displays 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Route that displays an HTML page with 'Number: n' inside an H1 tag if n is an integer."""
    if isinstance(n, int):
        return render_template_string('<!DOCTYPE html>\n'
                                      '<HTML lang="en">\n'
                                      '    <HEAD>\n'
                                      '        <TITLE>HBNB</TITLE>\n'
                                      '    </HEAD>\n'
                                      '    <BODY>\n'
                                      '        <H1>Number: {{ n }}</H1>\n'
                                      '    </BODY>\n'
                                      '</HTML>', n=n)
    else:
        return 'Not Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
