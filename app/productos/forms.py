from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,StringField, IntegerField
class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese nombre del producto")
    precio =IntegerField("Ingrese el precio del producto")
    submit =SubmitField("Guardar")