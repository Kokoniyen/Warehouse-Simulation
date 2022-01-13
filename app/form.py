from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields import TelField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError


class SimulationForm(FlaskForm):
    roomTemp = StringField("Room Temperature", validators=[DataRequired()])
    roomPress = StringField("Room Pressure", validators=[DataRequired()])
    submit = SubmitField("Evaluate")
