from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Email,ValidationError,EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password =PasswordField('Password',validators=[DataRequired()])
    password2=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')

    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('please use a diferent username')

    def validate_email(self,email):
        user =User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('email already used')

