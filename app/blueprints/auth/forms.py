from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField ('Password: ', validators=[DataRequired()])
    submit_btn = SubmitField('Login to Poke-Class')


class SignUpForm(FlaskForm):
    username = StringField('First Name: ', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField('Become a Trainer')