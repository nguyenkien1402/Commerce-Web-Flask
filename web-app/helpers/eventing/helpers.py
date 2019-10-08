from utilities import firebase_config

import os
import json
import time

from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()

#GCP_PROJECT = os.environ.get('GCP_PROJECT')
GCP_PROJECT = firebase_config.GCP_PROJECT

def stream_event(topic_name, event_type, event_context):
    """
    Helper function for publishing an event
    :params
        topic_name: the name of the Cloud Pub/Sub topic.
        event_type: the type of the event.
        event_context: the context of the event.
    :return:
        None
    """
    topic_path = publisher.topic_path(GCP_PROJECT, topic_name)
    request = {
        'event_type': event_type,
        'created_time': str(int(time.time())),
        'event_context': event_context
    }
    data = json.dumps(request).encode()
    publisher.publish(topic_path, data)

