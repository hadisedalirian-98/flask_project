from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from blog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=4,max=25,message ='username must be more 4 character')])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password',message ='password must be mach')])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
           raise ValidationError('this username already exist')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
           raise ValidationError('this email already exist')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')
    remember=BooleanField('Remember me')


class UpdateProfileForm(FlaskForm):
     username = StringField('Username',validators=[DataRequired(),Length(min=4,max=25,message ='username must be more 4 character')])
     email=StringField('Email',validators=[DataRequired(),Email()])

     def validate_username(self, username):
        if username.data != current_user.username:
           user = User.query.filter_by(username=username.data).first()
           if user:
              raise ValidationError('this username already exist')
        

     def validate_email(self, email):
        if email.data != current_user.email:
           user = User.query.filter_by(email=email.data).first()
           if user:
              raise ValidationError('this email already exist')
           


class PostForm(FlaskForm):
    title=StringField('Tilte',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])

