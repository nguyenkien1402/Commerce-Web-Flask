

from dataclasses import asdict
import time

from google.cloud import firestore
from .data_classes import CartItem

firestore_client = firestore.Client()

def get_cart(uid):
    """
    Helper function for getting all the items in a cart
    :param
        uid: the unique id of the user
    :return:
        A list of CartItem
    """

    cart = []
    query_results = firestore_client.collection('carts').where('uid','==',uid).order_by('modify_item', direction=firestore.Query.DESCENDING).get()
    for result in query_results:
        item = CartItem.deserialize(result)
        cart.append(item)
    return cart