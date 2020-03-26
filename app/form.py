from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed,FileField
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email, DataRequired
from wtforms.widgets import Input

from werkzeug.utils import secure_filename


class ProfileForm(FlaskForm):
    first_name = StringField('fname', validators=[InputRequired(), Length(max=30)])
    last_name = StringField('lname', validators=[InputRequired(), Length(max=30)])
    gender = SelectField('gender', choices=[ ('2', 'Male'), ('1', 'Female')], validators=[InputRequired()])
    email = EmailField('email', validators=[Email(), InputRequired(), Length(max=50)])
    location = StringField('location', validators=[InputRequired(), Length(max=50)])
    bio = TextAreaField('bio', validators=[DataRequired(), Length(max=150)])
    photo= FileField('photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only!')])
