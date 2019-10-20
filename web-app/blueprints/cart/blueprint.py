from flask import Blueprint, render_template, redirect, request
from helpers import carts, product_catalog
from middlewares.auth import auth_optional, auth_required

cart_page = Blueprint('cart_page',__name__)

@cart_page.route('/cart', methods=['GET'])
@auth_required
def display(auth_context):
    """
    View function for displaying the content of the carts
    :param
        auth_context: the authentication context of the request
    :return:
        render template
    """

    cart = carts.get_cart(auth_context.get('uid'))
    for item in cart:
        product = product_catalog.get_product(item.item_id)
        item.info = product

    return render_template('cart.html',
                           cart=cart,
                           auth_context=auth_context,
                           bucket=product_catalog.BUCKET)

@cart_page.route('/cart', methods=['POST'])
@auth_required
def add(auth_context):
    """
    Endpoint function for adding item to the cart
    :param
        auth_context: the authentication context of the request
    :return:
        Text message with HTTP status code 200
    """
    print("Add")
    uid = auth_context.get('uid')
    item_id = request.form.get('id')
    if item_id:
        print("item_id: "+item_id)
        carts.add_to_cart(uid,item_id)
        return "Operation Completed", 200
    return "Operation Failed", 400


@cart_page.route('/cart', methods=['DELETE'])
@auth_required
def remove(auth_context):
    """
    Endpoint for removing an item from cart
    :param
        auth_context: the authentication context of request
    :return:
        Text message with HTTP status code 200
    """
    uid = auth_context.get('uid')
    item_id = request.form.get('id')
    print("Remove:"+item_id)
    if item_id:
        carts.remove_from_cart(uid, item_id)
        return "Operation Completed", 200
    return "Operation Failed", 400
