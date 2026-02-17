from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="We need your name, it cannot be empty!")]) #Custom message for showing 
    email = StringField("Email", validators=[DataRequired(message="Please enter your mail, you cannot done empty !"), Email()])
    password = PasswordField("Password", validators=[DataRequired(message="Please enter atleast 8 Digit Password !"), Length(min=8)])
    submit = SubmitField("Register")