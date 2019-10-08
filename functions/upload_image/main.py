
# This is a function which is used in google cloud function
# to upload image

import os
import uuid

from google.cloud import storage
from wand.image import Image

client = storage.Client()

# BUCKET = os.environ.get('GCS_BUCKET')
BUCKET = "commerce-store-serverless.appspot.com"
FILENAME_TEMPLATE = '{}.png'
EXPECTED_WIDTH = 640
EXPECTED_HEIGHT = 640

def upload_image(request):
    # Set up CORS to allow requests from arbitrary origins.
    # See https://cloud.google.com/functions/docs/writing/http#handling_cors_requests
    # for more information.
    # For maxiumum security, set Access-Control-Allow-Origin to the domain
    # of your own.
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Max-Age': '3600'
        }

        return ('',204,headers)

    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    file = request.files.get('filepond')
    if not file:
        return ("File is not found in the request", 400, headers)

    data = file.read()

    with Image(blob=data) as image:
        image.transform(resize="{}x{}>".format(EXPECTED_WIDTH, EXPECTED_HEIGHT))
        image.extent(
            width=EXPECTED_WIDTH,
            height=EXPECTED_HEIGHT,
            x=int((EXPECTED_WIDTH - image.width)/2),
            y=-int((EXPECTED_HEIGHT - image.height)/2)
        )
        converted_image = image.make_blob(format='png')

    id = uuid.uuid4().hex
    filename = FILENAME_TEMPLATE.format(id)

    bucket = client.get_bucket(BUCKET)
    blob = bucket.blob(filename)

    blob.upload_from_string(converted_image, content_type='image/png')
    return(id, 200, headers)