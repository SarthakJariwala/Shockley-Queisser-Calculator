from flask_wtf import FlaskForm
from wtforms import DecimalField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SQ_Form(FlaskForm):
    bandgap = DecimalField(
        "Bandgap (eV)", 
        validators = [DataRequired()], 
        places=2
    )

    temperature = DecimalField(
        "Cell Temperature (K)", 
        validators = [DataRequired()], 
        places=2
    )

    submit = SubmitField("Calculate")

    output = TextAreaField(
        "Shockley-Quesisser Efficiency Limit is :",
        render_kw={'rows':5})