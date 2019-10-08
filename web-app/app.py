from flask import Flask
import firebase_admin
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Commerce-Store-Serverless.json'

firebase = firebase_admin.initialize_app()
app = Flask(__name__)

from blueprints import *


app.register_blueprint(signin_page)
app.register_blueprint(product_catalog_page)
app.register_blueprint(cart_page)
app.register_blueprint(sell_page)

# this one is for register secret key to flask in order to use form submission
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == '__main__':
    app.run(debug=True)
