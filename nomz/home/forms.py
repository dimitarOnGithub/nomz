from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewCategoryForm(FlaskForm):
    name = StringField('Category Title', validators=[DataRequired()])
    blurb = StringField('Short Description', validators=[DataRequired()])
    submit = SubmitField('Create')


class NewRecipeForm(FlaskForm):
    name = StringField('Recipe Title', validators=[DataRequired()])
    summary = StringField('Short Summary', validators=[DataRequired()])
