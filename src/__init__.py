import argparse
import logging
import yaml
import os
from serializers import *

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)

SERIALIZERS = {
    "pickle": PickleSerializer,
    "xml": BasicSerializer,
    "json": JsonSerializer,
    "proto": BasicSerializer,
    "avro": BasicSerializer,
    "yaml": BasicSerializer,
    "msgpack": BasicSerializer,
}

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--format",
    choices=SERIALIZERS.keys(),
    type=str,
    help="Format for serializer, required for serializer target"
)

parser.add_argument(
    "-t",
    "--target",
    choices=["serializer", "proxy"],
    required=True,
    type=str,
    help="Specifying target to run, required"
)

parser.add_argument(
    "-c",
    "--config",
    type=str,
    help="Config for proxy server, only for proxy server",
    default="config.yaml"
)

args = parser.parse_args()

DATA_FORMAT = args.format
TARGET = args.target
SERIALIZER_SETTINGS = None
CONFIG = None

for path in [args.config, os.path.join(args.config)]:
    if os.path.isfile(path):
        with open(path) as file:
            logging.info(f"Read config from {path}")
            config = file.read()
            break

if config is None:
    raise f"Bad config path {args.config}"

CONFIG = yaml.load(config, Loader=yaml.CLoader)
SERIALIZERS_SETTINGS = {}

for data_format in SERIALIZERS.keys():
    if data_format in CONFIG["serializers"]:
        SERIALIZERS_SETTINGS[data_format] = SerializerSettings(CONFIG["serializers"][data_format]["port"])
    else:
        SERIALIZERS_SETTINGS[data_format] = None
