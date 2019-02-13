from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Feedback,Pitch
from .forms import FeedbackForm,PitchForm
from .. import db

# landing
@main.route('/')
def index():

    title = 'Home Page - Get The latest Pitch stories'
    return render_template('index.html',title = title)

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
def product():
    product_pitch=Pitch.query.filter_by(category="PROMOTION")
    return render_template('product.html', product_pitch = product_pitch)
