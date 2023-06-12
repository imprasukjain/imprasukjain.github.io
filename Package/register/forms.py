from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "Enter Username"})
    email=StringField('Email',validators=[DataRequired(),Email()], render_kw={"placeholder": "Enter Email"})
    Mobile = IntegerField('Mobile',validators=[DataRequired()], render_kw={"placeholder": "Enter Mobile Number"})
    submit=SubmitField('SUBMIT')
    
class ResultsForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "Enter Name"})
    marks=IntegerField('Marks',validators=[DataRequired()],render_kw={"placeholder": "Enter Marks"})
    submit=SubmitField('SUBMIT')
