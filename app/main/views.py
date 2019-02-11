from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():

    title = 'Home Page - Get The latest Pitch stories'
    return render_template('index.html',title = title)

# @main.route('/***/pitch/new', methods = ['GET','POST'])
# @login_required
# def new_pitch():
