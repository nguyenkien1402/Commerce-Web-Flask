

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


def add_to_cart(uid, item_id):
    """
    Helper function for adding an item to a cart
    :param
        uid: the unique ID of the user
        item_id: the ID of the item
    :return:
        None.
    """
    item = CartItem(
        uid=uid,
        item_id=item_id,
        modify_time=int(time.time())
    )
    firestore_client.collection('carts').document().set(asdict(item))


def remove_from_cart(uid, item_id):
    """
    Helper function to remove an item from cart
    :param
        uid: the unique ID of the user
        item_id: the ID of the item
    :return:
        None
    """
    transaction = firestore_client.transaction()

    @firestore.transactional
    def transactional_remove_from_cart(transaction, uid, item_id):
        query_result = firestore_client.collection("carts").where('uid', '==', uid).where('item_id', '==', item_id).get()
        for result in query_result:
            reference = firestore_client.collection('carts').document(result.id)
            transaction.delete(reference)

    transactional_remove_from_cart(transaction, uid, item_id)