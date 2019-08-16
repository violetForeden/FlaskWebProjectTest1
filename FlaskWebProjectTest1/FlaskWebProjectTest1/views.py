"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,redirect,url_for
from FlaskWebProjectTest1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/hello/<guest>')
def hello_guest(guest):
    """hello page"""
    return 'Hello %s!' % guest

@app.route('/admin')
def hello_admin():
    return 'Hello admin!'

@app.route('/user/')
def no_user():
    return 'No user!'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    elif name != None:
        return redirect(url_for('hello_guest',guest = name))
    