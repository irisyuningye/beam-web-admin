from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, FormField
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
    noteContent = PasswordField('Content', validators=[DataRequired()])

