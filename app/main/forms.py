from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class FeedbackForm(FlaskForm):

    title = StringField('Feedback title',validators=[Required()])

    feedback = TextAreaField('Pitch feedback', validators=[Required()])

    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
