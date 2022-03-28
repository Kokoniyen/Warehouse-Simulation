import os
from unittest import result
from app import app
import pandas as pd
from app.mold_func import get_temp_varies
from flask import render_template, session, redirect, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from app.form import SimulationForm, GridForm
from app.form import PalletForm, DoorForm

data_df = pd.read_csv("app/static/data.csv", sep="\t")


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SimulationForm()
    if form.validate_on_submit():
        session["heatConductivity"] = form.heatConductivity.data
        session["roomTemp"] = form.roomTemp.data
        session["roomLength"] = form.roomLength.data
        session["roomBreadth"] = form.roomBreadth.data
        session["roomHeight"] = form.roomHeight.data
        session["numHours"] = form.numHours.data
        session["result"] = None
        return redirect(url_for("grid_page"))

    return render_template("index.html", form=form)


@app.route("/grid_page", methods=["GET", "POST"])
def grid_page():
    form = GridForm()
    if form.validate_on_submit():
        return redirect(url_for("pallet_location"))

    return render_template("grid_page.html", form=form)


@app.route("/pallet_location", methods=["GET", "POST"])
def pallet_location():
    form = PalletForm()
    if form.validate_on_submit():
        return redirect(url_for("door_location"))
    return render_template("pallet_location.html", form=form)


@app.route("/door_location", methods=["GET", "POST"])
def door_location():
    form = DoorForm()
    if form.validate_on_submit():
        print("validates")
        session["result"] = get_temp_varies(
            Heat_conductivity_of_walls=float(session["heatConductivity"]),
            Initial_Temperature=int(session["roomTemp"]),
            Length=int(session["roomLength"]),
            Breadth=int(session["roomBreadth"]),
            Height=int(session["roomHeight"]),
            Number_of_hours_to_run_simulation=int(session["numHours"]),
        )
        return render_template(
            "door_location.html", form=form, result=session["result"]
        )
    return render_template("door_location.html", form=form)
