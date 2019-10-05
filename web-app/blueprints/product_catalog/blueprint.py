from flask import render_template, Blueprint
from middlewares.auth import *
from helpers import product_catalog


product_catalog_page = Blueprint('product_catalog_page',__name__)

@product_catalog_page.route('/')
@auth_required
def display(auth_context):
    """
    View function for displaying product catalog
    :param
        auth_context: the authentication context of request
    :return:
        Rendered HTML page
    """

    # Get products
    products = product_catalog.list_product()
    # Get promoted product by recommendation
    # promos = product_catalog.get_promos()
    return render_template('product_catalog.html',
                           products=products,
                           promos=None,
                           auth_context=auth_context,
                           bucket=product_catalog.BUCKET)