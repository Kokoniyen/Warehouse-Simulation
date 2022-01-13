import os
from app import app
from flask import render_template, redirect, url_for
from app.form import SimulationForm


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SimulationForm()
    if form.validate_on_submit():
        result = int(form.roomTemp.data) * int(form.roomPress.data)
        form.roomTemp.data = ""
        form.roomPress.data = ""
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], "cuboid.gif")
        print(file_path)
        return render_template("index.html", form=form, result=file_path)

    return render_template("index.html", form=form)
