from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=5)])
    email = StringField('E-mail',
                        [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password',
                             [validators.DataRequired(),
                              validators.EqualTo(
                                  'confirm_password',
                                  message='Field must be equal to password')])
    confirm_password = PasswordField('Password Confirm',
                                     [validators.DataRequired()])
    submit = SubmitField('Register')


class UserLoginForm(FlaskForm):
    email = StringField('E-mail',
                        [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')
