from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from flaskblog.models import User

class Registerform(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    comfir_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_user_name(self,user_name):
        user = User.query.filter_by(user_name = user_name.data).first()
        if user:
            raise ValidationError("That username already exists, choose something different please")

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("That email already exists, choose something different please")

class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    remember = BooleanField('Remember Me')
    password = PasswordField('Password', validators=[DataRequired(),])
    submit = SubmitField('Login')
