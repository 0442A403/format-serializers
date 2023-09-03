import argparse
import logging
import os.path
import requests
from __init__ import SERIALIZERS

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--format",
    choices=SERIALIZERS.keys(),
    type=str,
    help="format of data",
    required=True,
)

parser.add_argument(
    "-a",
    "--action",
    choices=["serialize", "deserialize", "full"],
    type=str,
    help="serialize or deserialize data",
    required=True,
)

parser.add_argument(
    "-d",
    "--data",
    type=str,
    help="Path or string data to send",
    required=True,
)


def make_request(action, data_format, data):
    addr = f"{SERIALIZERS[data_format].addr}/{action}"
    json_data = {
        "format": data_format,
        "data": "".join(map(chr, data)),
    }

    result = requests.get(addr, json=json_data)

    logging.info(f"Status code: {result.status_code}")
    if result.status_code == 200:
        logging.info(f"Result:\n{result.content}")
        return result.content
    else:
        raise "Something went wrong"


args = parser.parse_args()

if os.path.exists(args.data):
    with open(args.data) as file:
        logging.info(f"Read data from {args.data}")
        args.data = file.read()
elif os.path.exists(os.path.join(os.getcwd(), args.data)):
    with open(os.path.join(os.getcwd(), args.data)) as file:
        logging.info(f"Read data from {os.path.join(os.getcwd(), args.data)}")
        args.data = file.read()

args.data = args.data.encode()


if args.action != "full":
    make_request(args.action, args.format, args.data)
else:
    serialized = make_request("serialize", args.format, args.data)
    deserialized = make_request("deserialize", args.format, serialized)
