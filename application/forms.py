from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description',validators=[DataRequired()])
    price = StringField('price', validators = [DataRequired()])
    quantity = StringField('quantity', validators = [DataRequired()])
    submit = SubmitField("Submit")