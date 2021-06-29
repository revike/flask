from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, TextAreaField, \
    SelectMultipleField


class CreateArticleForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    text = TextAreaField('Text', [validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Create Article')
