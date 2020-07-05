from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, TextAreaField
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

    output = TextAreaField("Shockley-Quesisser Limit")