import logging
from flask import Flask, request
from __init__ import SERIALIZERS


app = Flask(__name__)
app.debug = True

format = None
serializer = None


@app.route("/serialize")
def serialize():
    logging.info(f"Got /serialize request")
    data = request.get_json()

    if data["format"] != format:
        #return f"Server accepts only {format} format", 400
        pass

    serialized = SERIALIZERS[format].serialize(data["data"])
    return serialized



@app.route("/deserialize")
def deserialize():
    logging.info(f"Got /deserialize request")
    data = request.get_json()
    print(data['data'].encode())

    if data["format"] != format:
        #return f"Server accepts only {format} format", 400
        pass

    deserialized = SERIALIZERS[format].deserialize(data["data"])
    return deserialized.encode()


def start_server(format_):
    global format
    format = format_
    global serializer
    serializer = SERIALIZERS[format]
    app.run()
