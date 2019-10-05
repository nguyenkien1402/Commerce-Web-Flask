import os
from google.cloud import firestore

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Commerce-Store-Serverless.json'
firestore_client = firestore.Client()

