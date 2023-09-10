import argparse
import json
import logging
import os.path
import requests
import yaml
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

parser = argparse.ArgumentParser()

FORMATS = ["pickle", "xml", "json", "proto", "yaml", "msgpack", "avro"]

parser.add_argument(
    "-f",
    "--format",
    choices=FORMATS + ["all"],
    type=str,
    help="format of data",
    required=False,
)

parser.add_argument(
    "-a",
    "--action",
    choices=["serialize", "deserialize", "full", "get_result"],
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
            logging.debug(f"Read config from {path}")
            config = file.read()
            break

if config is None:
    raise f"Bad config path {args.config}"

config = yaml.load(config, Loader=yaml.CLoader)


def make_request(action, data, data_format=None, test_run=1000):
    addr = f"http://127.0.0.1:2000/{action}"
    if action == "get_result":
        json_data = {
            "data": "".join(map(chr, data)),
            "test_runs": test_run
        }
    else:
        json_data = {
            "format": data_format,
            "data": "".join(map(chr, data)),
        }

    result = requests.get(addr, json=json_data)

    logging.debug(f"Status code: {result.status_code}")
    if result.status_code == 200:
        if action == "serialize":
            logging.debug(f"Result:\n{result.content}")
            return result.content
        else:
            logging.debug(f"Result:\n{json.dumps(json.loads(result.content), indent=4)}")
            return json.loads(result.content)
    else:
        raise "Something went wrong"

for path in [args.data, os.path.join(os.getcwd(), args.data)]:
    if os.path.isfile(path):
        with open(args.data) as file:
            logging.debug(f"Read data from {path}")
            args.data = file.read()
            break

args.data = args.data.encode()

data_formats = [args.format] if args.format != "all" else FORMATS

for data_format in data_formats:
    if args.action == "get_result":
        result = make_request("get_result", args.data)
        for data_format, stats in result.items():
            byte_size = stats['byte_size']
            ser_time = stats["average_serialize_time"]
            deser_time = stats["average_deserialize_time"]
            logging.info(f"{data_format}\t{byte_size} bytes\t% 5.3f ms\t%.3f ms", ser_time / 1000, deser_time / 1000)
    elif args.action == "full":
        time_start = time.time()
        serialized = make_request("serialize", args.data, data_format)
        time_serialization = time.time()
        deserialized = make_request("deserialize", serialized, data_format)
        time_end = time.time()
        logging.info(f"{data_format}:\t{len(serialized)}\t%.2fms\t%.2fms",
                     (time_serialization - time_start) * 1000,
                     (time_end - time_serialization) * 1000)
    else:
        time_start = time.time()
        data = make_request(args.action, args.data, data_format)
        time_end = time.time()
        logging.info(f"{data_format}:\t{len(data)}\t%.2fms", (time_end - time_start) * 1000)
