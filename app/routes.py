""" 1. Routes are the different URLs that my application (i.e., app, being the 
sub-directory 'app') implements. In Flask, handlers for the application routes
are written as Python functions, called view functions. View functions are 
mapped to one or more route URLs so that Flask knows what logic to execute when 
a client requests a given URL.
2. Flask makes extensive use of decorators.  A decorator modifies the function 
that follows it.
3. The order in which decorators are written matters.
"""

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app    # import app variable, which is a member of app package.

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Deep Learning in Finance')


