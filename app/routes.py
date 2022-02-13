import os
from app import app
import pandas as pd
from app.mold_func import get_temp_varies
from flask import render_template, redirect, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from app.form import SimulationForm

data_df = pd.read_csv("app/static/data.csv", sep="\t")


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SimulationForm()
    if form.validate_on_submit():
        result = get_temp_varies(
            Heat_conductivity_of_walls=float(form.heatConductivity.data),
            Initial_Temperature=int(form.roomTemp.data),
            Length=int(form.roomLength.data),
            Breadth=int(form.roomBreadth.data),
            Height=int(form.roomHeight.data),
        )
        return render_template("index.html", form=form, result=result)

    return render_template("index.html", form=form)
