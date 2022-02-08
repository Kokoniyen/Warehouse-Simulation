import os
from app import app
import pandas as pd
from flask import render_template, redirect, url_for
from app.form import SimulationForm

data_df = pd.read_csv("app/static/data.csv", sep="\t")


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SimulationForm()
    if form.validate_on_submit():
        result = int(form.roomTemp.data) * int(form.roomPress.data)
        form.roomTemp.data = ""
        form.roomPress.data = ""
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], "cuboid.gif")
        print(data_df.iloc[0])
        pi = data_df.iloc[0]["Value"]
        radius = data_df.iloc[1]["Value"]
        return render_template(
            "index.html", form=form, result=file_path, pi=pi, radius=radius
        )

    return render_template("index.html", form=form)
