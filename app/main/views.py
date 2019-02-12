from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import Reviews, User

@main.route('/')
def index():

    title = 'Home Page - Get The latest Pitch stories'
    return render_template('index.html',title = title)

# @main.route('/***/pitch/new', methods = ['GET','POST'])
# @login_required
# def new_pitch():

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
