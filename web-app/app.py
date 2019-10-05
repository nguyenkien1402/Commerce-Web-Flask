from flask import Flask
import firebase_admin
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Commerce-Store-Serverless.json'

firebase = firebase_admin.initialize_app()
app = Flask(__name__)

from blueprints import *


app.register_blueprint(signin_page)
app.register_blueprint(product_catalog_page)

if __name__ == '__main__':
    app.run(debug=True)
