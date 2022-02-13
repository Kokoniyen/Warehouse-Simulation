from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields import TelField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError


class SimulationForm(FlaskForm):
    roomTemp = StringField("Initial Temperature", validators=[DataRequired()])
    roomLength = StringField("Room Length", validators=[DataRequired()])
    roomBreadth = StringField("Room Breadth", validators=[DataRequired()])
    roomHeight = StringField("Room Height", validators=[DataRequired()])
    heatConductivity = StringField(
        "Heat Conductivity of Walls", validators=[DataRequired()]
    )

    submit = SubmitField("Evaluate")
