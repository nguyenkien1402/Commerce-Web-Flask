from flask import Blueprint, render_template, redirect
from middlewares.auth import *
from middlewares.forms_validation import *
from helpers import product_catalog
import time

sell_page = Blueprint('sell_page',__name__)

@sell_page.route('/sell', methods=['GET'])
@auth_required
def display(auth_context):
    """
    View function for displaying the sell page
    :return:
        Render HTML Template
    """
    form = SellForm()
    return render_template('sell.html', auth_context=auth_context, form=form)


@sell_page.route('/sell', methods=['POST'])
@auth_required
@sell_form_validation_required
def proccess(auth_context, form):
    """
    View function for processing sell request
    :param
        auth_context: the authentication request of the request
        form: a validated sell form
    :return:
        Render HTML Page
    """
    product = product_catalog.Product(name=form.name.data,
                                      description=form.description.data,
                                      image=form.image.data,
                                      labels=[],
                                      price=form.price.data,
                                      created_at=int(time.time()))
    product_id = product_catalog.add_product(product)

    return redirect('/sell')