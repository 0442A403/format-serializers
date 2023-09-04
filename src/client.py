import argparse
import logging
import os.path
import requests
import yaml

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--format",
    choices=["pickle", "xml", "json", "proto", "avro", "yaml", "msgpack"],
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
    print(result.status_code)
    if result.status_code == 200:
        logging.info(f"Result:\n{result.content}")
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

if args.action != "full":
    make_request(args.action, args.format, args.data)
else:
    serialized = make_request("serialize", args.format, args.data)
    deserialized = make_request("deserialize", args.format, serialized)
