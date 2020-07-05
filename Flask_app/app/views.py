from flask import render_template, redirect, url_for
from app import app, forms, calculate

@app.route("/", methods=["GET", "POST"])
def index():
    form = forms.SQ_Form()
    if form.validate_on_submit():
        bandgap = form.bandgap.data
        temp = form.temperature.data
        form.output.data = calculate.calculate_SQ(bandgap, temp)
    return render_template("index.html", form=form)
