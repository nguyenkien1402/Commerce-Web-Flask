
from functools import wraps

from flask_wtf import FlaskForm
from wtforms import FieldList, FloatField, StringField
from wtforms.validators import DataRequired, Optional

class SellForm(FlaskForm):
    """
    Flask form for selling item
    """
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired()])
    image = StringField('image', validators=[DataRequired()])


def sell_form_validation_required(f):
    """
    A decorator for validating requess with the sell form
    Return an error message if validation fails
    :param
        f: the view function to decorate
    :return:
        decorated function
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        sell_form = SellForm()
        if not sell_form.validate():
            return "Something does not look right, please check your the input and try again"

        return f(form=sell_form,*args, **kwargs)
    return decorated