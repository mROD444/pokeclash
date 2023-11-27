from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TeamForm(FlaskForm):
    pokemon1 = StringField('Enter your first pokemon: ', validators=[DataRequired()])
    pokemon2 = StringField('Enter your second pokemon: ', validators=[DataRequired()])
    pokemon3 = StringField('Enter your third pokemon: ', validators=[DataRequired()])
    pokemon4 = StringField('Enter your fourth pokemon: ', validators=[DataRequired()])
    pokemon5 = StringField('Enter your fifth pokemon: ', validators=[DataRequired()])