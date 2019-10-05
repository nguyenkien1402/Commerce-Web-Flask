from dataclasses import asdict
import os
import uuid
from utilities import firebase_config

from google.cloud import firestore
from .data_classes import Product, PromoEntry

# BUCKET = os.environ.get('GCS_BUCKET')
BUCKET = firebase_config.GCS_BUCKET


firestore_client = firestore.Client()

def add_product(product):
    """
    Helper function to add product
    :param
        product: A product object
    :return:
        the ID of the product
    """
    product_id = uuid.uuid4().hex
    firestore_client.collection('products').document(product_id).set(asdict(product))
    return product_id

def get_product(product_id):
    """
    Helper function to get the product by its id
    :param
        product_id: The id of the product
    :return:
        a product object
    """
    product = firestore_client.collection('products').document(product_id).get()
    return Product.deserialize(product)

def list_product():
    """
    Helper function to retrieve list of product
    :return:
        A list of product
    """
    products = firestore_client.collection('products').order_by('created_at').get()
    product_list =[Product.deserialize(product) for product in list(products)]
    return product_list


def calculate_total_price(product_ids):
    """
    Helper function to calculate total price of all the product
    :param
        product_ids: list id of the product
    :return:
        the total price
    """
    total = 0
    for product_id in product_ids:
        product = get_product(product_id)
        total += product.price
    return total

def get_promos():
    """
    Helper function for getting promoted products
    :return:
        A list of product object
    """
    promos = []
    query = firestore_client.collection('promos').where('label', '==', 'pets').where('score', '>=', "0.7")
    query = query.order_by('score', direction=firestore.Query.DESCENDING).limit(3)
    query_result = query.get()
    for result in query_result:
        entry = PromoEntry.deserialize(result)
        product = get_product(entry.id)
        promos.append(product)
    return promos