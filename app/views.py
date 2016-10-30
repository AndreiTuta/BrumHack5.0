from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html',title='Home',)


@app.route('/machine')
def machine():
    return render_template('machine.html',title='Home',)
