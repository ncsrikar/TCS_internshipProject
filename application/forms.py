from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,DateTimeField,SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    rememberme = BooleanField("rememberme")
    submit = SubmitField("login")

class Register(FlaskForm):
    patient_ssn_id = IntegerField("Patient SSN ID", validators=[DataRequired()])
    name = StringField("Name",validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    date = DateTimeField("Date",validators=[DataRequired()],format='%Y-%m-%dT%H:%M')
    type = SelectField("Type", choices=[('General ward','General ward'),('Semi Sharing','Semi Sharing'),('Single Room','Single Room')])
    address = StringField("Address",validators=[DataRequired()])
    city = StringField("City",validators=[DataRequired()])
    state = StringField("State",validators=[DataRequired()])
    submit = SubmitField("register")

class GetPatientInfo(FlaskForm):
    patient_id = IntegerField("Patient ID", validators=[DataRequired()])
    submit_get_details = SubmitField("Get Patient Details")

class UpdatePatientInfo(FlaskForm):
    patient_id_got = IntegerField("Patient ID", validators=[DataRequired()])
    patient_ssn_id = IntegerField("Patient SSN ID", validators=[DataRequired()])
    name = StringField("Name",validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    type = SelectField("Type", choices=[('General ward','General ward'),('Semi Sharing','Semi Sharing'),('Single Room','Single Room')])
    address = StringField("Address",validators=[DataRequired()])
    city = StringField("City",validators=[DataRequired()])
    state = StringField("State",validators=[DataRequired()])
    submit_update = SubmitField("Update Patient Details")