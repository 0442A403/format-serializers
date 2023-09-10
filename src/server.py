import logging
import os
import json
import time

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

    serialized = serializer.serialize(json.loads(data["data"]))
    return serialized



@app.route("/deserialize")
def deserialize():
    logging.info(f"Got /deserialize request")
    data = request.get_json()

    if data["format"] != data_format:
        return f"Server accepts only {data_format} format", 400

    deserialized = serializer.deserialize(data["data"])
    return deserialized


@app.route("/get_result")
def get_result():
    logging.info(f"Got /deserialize request")
    data = request.get_json()

    if data["format"] != data_format:
        return f"Server accepts only {data_format} format", 400

    test_runs = int(data["test_runs"])
    time_ser_sum = 0
    time_deser_sum = 0
    ser_byte_size = len(serializer.serialize(json.loads(data["data"])))

    data = json.loads(data["data"])
    for _ in range(test_runs):
        start_time = time.time_ns()
        ser = serializer.serialize(data)
        ser_time = time.time_ns()
        serializer.deserialize(ser, already_binary=True)
        deser_time = time.time_ns()

        time_ser_sum += ser_time - start_time
        time_deser_sum += deser_time - ser_time

    return {
        "byte_size": ser_byte_size,
        "average_serialize_time": time_ser_sum / test_runs,
        "average_deserialize_time": time_deser_sum / test_runs,
    }


def start_server(data_format_, port):
    global data_format
    data_format = data_format_

    global serializer
    serializer = SERIALIZERS[data_format]

    app.run(port=port, host="0.0.0.0")
