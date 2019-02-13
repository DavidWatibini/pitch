from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Feedback,Pitch
from .forms import FeedbackForm,PitchForm
from .. import db

# landing
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'Pitcher'

    index=Pitch.query.all()

    return render_template('index.html', title = title, index = index)

# post pitch
@main.route('/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(post=form.post.data,body=form.body.data,category=form.category.data)
        pitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html',form=form)

# profile
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# feedback
@main.route('/feedback/<int:id>', methods = ['GET','POST'])
@login_required
def new_feedback(id):
    form = FeedbackForm()
    pitch = Pitch.query.get(id)
    if fom.validate_on_submit():
        feedback = Feedback(title=form.title.data,feedback=form.feedback.data, pitch=pitch)
        db.session.add(feedback)
        db.session.commit()
    feed_back = Feedback.query.filter_by(pitch=pitch).all()
    return render_template('feedback.html',feed_back=feed_back,form=form)


# product
@main.route('/product', methods = ['GET','POST'])
@login_required
def product():
    product_pitch=Pitch.query.filter_by(category="PRODUCT")
    return render_template('product.html', product_pitch = product_pitch)

# pick_Up
@main.route('/pick_up', methods = ['GET','POST'])
@login_required
def pick():
    pick_Up=Pitch.query.filter_by(category="PICK-UP")
    return render_template('pick_up.html', pick_Up = pick_Up)

# stand up comedy
@main.route('/stand_up_comedy', methods = ['GET','POST'])
@login_required
def stand():
    stand_Up=Pitch.query.filter_by(category="COMEDY")
    return render_template('stand_up_comedy.html', stand_Up = stand_Up)

# PROMOTION
@main.route('/promotion', methods = ['GET','POST'])
@login_required
def promotion():
    promotion_pitch=Pitch.query.filter_by(category="PROMOTION")
    return render_template('promotion.html', promotion_pitch = promotion_pitch)

# INTERVIEW
@main.route('/interview', methods = ['GET','POST'])
@login_required
def interview():
    interview_pitch=Pitch.query.filter_by(category="INTERVIEW")
    return render_template('interview.html', interview_pitch = interview_pitch)
