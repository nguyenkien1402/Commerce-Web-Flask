
from functools import wraps

from flask_wtf import FlaskForm
from wtforms import FieldList, FloatField, StringField, IntegerField
from wtforms.validators import DataRequired, Optional

class SellForm(FlaskForm):
    """
    Flask form for selling item
    """
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired()])
    image = StringField('image', validators=[DataRequired()])

class CheckOutForm(FlaskForm):
    """
    Flask form for checking out items.
    """
    product_ids = FieldList(StringField('product_id', validators=[DataRequired()]), min_entries=1)
    address_1 = StringField("address_1", validators=[DataRequired()])
    address_2 = StringField("address_2", validators=[Optional()])
    city = StringField("city", validators=[DataRequired()])
    state = StringField("state", validators=[DataRequired()])
    zip_code = IntegerField("zip_code", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    mobile = StringField("mobile", validators=[DataRequired()])
    stripeToken = StringField("stripeToken", validators=[DataRequired()])

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


def checkout_for_validation_required(f):
    """
    A decorated for validating requests with the check out form
    Returns an error message if validation fail
    :param f: the view function to decorate
    :return:
        decorated: the decorated function
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        checkout_form = CheckOutForm()
        if not checkout_form.validate():
            return "Something does not look right, check your input and try again", 400
        return f(form=checkout_form, *args, **kwargs)
    return decorated