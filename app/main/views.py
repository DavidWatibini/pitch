from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Feedback
from .forms import FeedbackForm,UpdateProfile
from .. import db

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

@main.route('/pitch/feedback/new/', methods = ['GET','POST'])
def new_feedback():
    form = FeedbackForm()
    if form.validate_on_submit():

        feedback = form.feedback.data
        new_feedback = Feedback(user.username,user.email,feedback)
        new_feedback.save_feedback()
        return redirect(url_for('pitch'))

    title = f'{user.username} feedback'
    return render_template('new_feedback.html',title = title,feedback_form=form,user=user)


@main.route('/product')
def Product():

    # title = f'{movie.title}'
    # feedback = Feedback.Display_feedbacks()

    return render_template('product.html')
