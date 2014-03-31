from flask.ext.wtf import Form
from wtforms import FloatField, BooleanField, SubmitField
from wtforms.validators import Required

class CostForm(Form):
    mealcost = FloatField ('mealcost')
    taxcost = FloatField('taxcost')
    tipcost = FloatField('tipcost')
    submit = SubmitField('send')
