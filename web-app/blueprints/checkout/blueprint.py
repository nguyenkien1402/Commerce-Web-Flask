
from flask import Flask, redirect, Blueprint,render_template,url_for,request
from middlewares.auth import auth_optional
from middlewares.forms_validation import CheckOutForm, checkout_for_validation_required
from helpers import product_catalog, carts

checkout_page = Blueprint("checkout_page",__name__)


@checkout_page.route('/checkout')
@auth_optional
def display(auth_context):
    """
    View function for displaying the checkout page
    :param
        auth_context: the authentication context of request
    :return:
        render HTML page
    """
    products = []
    # Prepares the checkout form
    form = CheckOutForm()
    product_id = request.args.get("id")
    from_cart = request.args.get("from_cart")
    # check one single item if parameter id presents in the URL query string
    # checkout all the items in the user's cart if parameter from_cart is present
    # in the URL query string and parameter id is absent
    if product_id:
        product = product_catalog.get_product(product_id)
        products.append(product)
    elif from_cart:
        uid = auth_context.get('uid')
        cart = carts.get_cart(uid)
        for item in cart:
            product = product_catalog.get_product(item.item_id)
            products.append(product)

    if products:
        return render_template('checkout.html',
                               products=products,
                               auth_context=auth_context,
                               form=form,
                               bucket=product_catalog.BUCKET)
    return redirect('/')