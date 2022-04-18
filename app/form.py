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
    numHours = StringField("Number of Hours", validators=[DataRequired()])

    numWindows = StringField("Number of Windows", validators=[DataRequired()])
    numPallets = StringField("Number of Pallets", validators=[DataRequired()])
    numDoors = StringField("Number of Doors", validators=[DataRequired()])
    numVents = StringField("Number of Vents", validators=[DataRequired()])
    cont_inue = SubmitField("Continue")


class GridForm(FlaskForm):
    submit = SubmitField("Continue")


class PalletForm(FlaskForm):
    submit = SubmitField("Continue")


class DoorForm(FlaskForm):
    submit = SubmitField("Evaluate")
