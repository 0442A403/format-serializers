import argparse
import json
import logging
import os.path
import requests
import yaml

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)

parser = argparse.ArgumentParser()

FORMATS = ["pickle", "xml", "json", "proto", "yaml", "msgpack"]

parser.add_argument(
    "-f",
    "--format",
    choices=FORMATS + ["all"],
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

parser.add_argument(
    "-c",
    "--config",
    type=str,
    help="Config path",
    default="config.yaml"
)

args = parser.parse_args()

config = None
for path in [args.config, os.path.join(args.config)]:
    if os.path.isfile(path):
        with open(path) as file:
            logging.info(f"Read config from {path}")
            config = file.read()
            break

if config is None:
    raise f"Bad config path {args.config}"

config = yaml.load(config, Loader=yaml.CLoader)

def make_request(action, data_format, data):
    addr = f"http://127.0.0.1:5000/{action}"
    json_data = {
        "format": data_format,
        "data": "".join(map(chr, data)),
    }

    result = requests.get(addr, json=json_data)

    logging.info(f"Status code: {result.status_code}")
    if result.status_code == 200:
        if action == "serialize":
            logging.info(f"Result:\n{result.content}")
        else:
            logging.info(f"Result:\n{json.dumps(json.loads(result.content), indent=4)}")
        return result.content
    else:
        raise "Something went wrong"

for path in [args.data, os.path.join(os.getcwd(), args.data)]:
    if os.path.isfile(path):
        with open(args.data) as file:
            logging.info(f"Read data from {path}")
            args.data = file.read()
            break

args.data = args.data.encode()

data_formats = [args.format] if args.format != "all" else FORMATS

for data_format in data_formats:
    logging.info(f"Data format: {data_format}")
    if args.action != "full":
        make_request(args.action, data_format, args.data)
    else:
        serialized = make_request("serialize", data_format, args.data)
        deserialized = make_request("deserialize", data_format, serialized)
