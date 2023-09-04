import logging
import os

from flask import Flask, request
from __init__ import SERIALIZER_SETTINGS
import requests


proxy_app = Flask(__name__)
if os.getenv('DEBUG') is not None:
    proxy_app.debug = True


@proxy_app.route("/serialize")
def serialize():
    data = request.get_json()
    logging.info(f"Got /serialize request for {data['format']} format")

    addr = f"{SERIALIZER_SETTINGS[data['format']].addr}/serialize"
    response = requests.get(addr, json=request.json)
    return response.content, response.status_code


@proxy_app.route("/deserialize")
def deserialize():
    data = request.get_json()
    logging.info(f"Got /serialize request for {data['format']} format")

    addr = f"{SERIALIZER_SETTINGS[data['format']].addr}/deserialize"
    response = requests.get(addr, json=request.json)
    return response.content, response.status_code


def start_proxy_server(port):
    proxy_app.run(port=port, host="0.0.0.0")
