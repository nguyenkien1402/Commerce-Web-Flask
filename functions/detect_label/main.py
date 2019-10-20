
# This is a function which is used in google cloud function
# to upload image

import os
import uuid
import base64
import json

from google.cloud import storage
from google.cloud import vision
from google.cloud import firestore

vision_client = vision.ImageAnnotatorClient()
firestore_client = firestore.Client()
BUCKET = "commerce-store-serverless.appspot.com"

def detect_label(data, context):
    if 'data' in data:
        request_json = base64.b64decode(data.get('data')).decode()
        request = json.loads(request_json)
        product_id = request.get('event_context').get('product_id')
        product_image = request.get('event_context').get('product_image')

        image = vision.types.Image()
        image.source.image_uri = 'gs://{}/{}'.format(BUCKET, product_image)
        response = vision_client.label_detection(image=image)
        labels = response.label_annotations
        top_labels = [label.description for label in labels[:3]]

        product_data =firestore_client.collection('products').document(product_id).get().to_dict()
        product_data['labels'] = top_labels
        firestore_client.collection('products').document(product_id).set(product_data)

    return ''