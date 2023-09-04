import logging
import os

from flask import Flask, request
from __init__ import SERIALIZERS


app = Flask(__name__)
if os.getenv('DEBUG') is not None:
    app.debug = True

data_format = None
serializer = None


@app.route("/serialize")
def serialize():
    logging.info(f"Got /serialize request")
    data = request.get_json()

    if data["format"] != data_format:
        return f"Server accepts only {data_format} format", 400

    serialized = serializer.serialize(data["data"])
    return serialized



@app.route("/deserialize")
def deserialize():
    logging.info(f"Got /deserialize request")
    data = request.get_json()

    if data["format"] != data_format:
        return f"Server accepts only {data_format} format", 400

    deserialized = serializer.deserialize(data["data"])
    return deserialized.encode()


def start_server(data_format_, port):
    global data_format
    data_format = data_format_

    global serializer
    serializer = SERIALIZERS[data_format]

    app.run(port=port, host="0.0.0.0")
