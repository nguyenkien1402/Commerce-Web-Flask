import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Commerce-Store-Serverless.json'

from google.cloud import firestore
import firebase_admin
from helpers.carts import *

firebase = firebase_admin.initialize_app()
firestore_client = firestore.Client()

if __name__ == '__main__':
    uid="TJFA2H1LUVMmySipYmXFDlRVZk62"
    carts = []
    queyry = firestore_client.collection('carts').where('uid', '==', uid).order_by('modify_time', direction=firestore.Query.DESCENDING).stream()
    for result in queyry:
        item = CartItem.deserialize(result)
        carts.append(item)
    print(len(carts))
# query_results = firestore_client.collection(u'carts').where(u'uid',u'==',uid).order_by('modify_item', direction=firestore.Query.DESCENDING).get()