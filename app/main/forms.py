from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class FeedbackForm(FlaskForm):

    title = StringField('Feedback title',validators=[Required()])

    feedback = TextAreaField('Pitch feedback', validators=[Required()])

    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('Pitch')
    category = SelectField('Pick Category',
                            choices=[('PRODUCT', 'PRODUCT'),
                                    ('INTERVIEW', 'INTERVIEW'),
                                    ('PICK-UP', 'PICK-UP'),
                                    ('PROMOTION', 'PROMOTION')],
                            validators=[Required()])
    submit = SubmitField('Pitch')
