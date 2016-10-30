from flask import render_template
from app import app
from BlackRock import *

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html',title='Home',)


@app.route('/machine')
def machine():
    temp = blackrock()
    print(temp)
    return render_template('machine.html',title='Home', sentData=temp)
