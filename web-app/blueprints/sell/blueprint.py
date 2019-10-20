from flask import Blueprint, render_template, redirect
from middlewares.auth import *
from middlewares.forms_validation import *
from helpers import product_catalog, eventing
import time
from utilities import firebase_config

sell_page = Blueprint('sell_page',__name__)
# PUBSUB_TOPIC_NEW_PRODUCT = os.environ.get('PUBSUB_TOPIC_NEW_PRODUCT')
PUBSUB_TOPIC_NEW_PRODUCT = firebase_config.PUBSUB_TOPIC_NEW_PRODUCT

@sell_page.route('/sell', methods=['GET'])
@auth_required
def display(auth_context):
    """
    View function for displaying the sell page
    :return:
        Render HTML Template
    """
    form = SellForm()
    return render_template('sell.html', auth_context=auth_context, form=form)


@sell_page.route('/sell', methods=['POST'])
@auth_required
@sell_form_validation_required
def proccess(auth_context, form):
    """
    View function for processing sell request
    :param
        auth_context: the authentication request of the request
        form: a validated sell form
    :return:
        Render HTML Page
    """
    product = product_catalog.Product(name=form.name.data,
                                      description=form.description.data,
                                      image=form.image.data,
                                      labels=[],
                                      price=form.price.data,
                                      created_at=int(time.time()))
    product_id = product_catalog.add_product(product)

    # Publish an event to the topic for new products
    # Cloud function detect_labels subscribes to the topic and labels the
    # product using Cloud Vision API upon arrival of new events
    # subscribe to the topic and save the event to BigQuery for
    # data analytics upon arrival of new events
    # ******The code below is for machine learning ***** #
    eventing.stream_event(
        topic_name=PUBSUB_TOPIC_NEW_PRODUCT,
        event_type='label_detection',
        event_context={
            'product_id': product_id,
            'product_image': product.image
        }
    )
    return redirect('/sell')