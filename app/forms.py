from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, FormField, TextAreaField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import EmailField
from .models import *
from flask_material import Material 

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email', validators = [DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])

class NoteForm(Form):           
    noteTitle = StringField('Title', validators=[DataRequired()])
    noteContent = TextAreaField('Content', validators=[DataRequired()])
    
class AccountSaveForm(Form):
    website_name = StringField('Website Name', validators=[DataRequired()])
    website_url = StringField('Website URL', validators=[DataRequired()])
    account_username = StringField('Account Name', validators=[DataRequired()])
    account_password = PasswordField('Account Password', validators=[DataRequired()])

