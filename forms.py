from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    price = FloatField('Price (INR)', validators=[DataRequired(), NumberRange(min=0)])
    qty = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save')

class OrderForm(FlaskForm):
    customer_name = StringField('Customer name', validators=[DataRequired()])
    customer_email = StringField('Customer email (optional)')
    submit = SubmitField('Place Order')
