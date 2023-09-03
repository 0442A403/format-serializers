import logging
from formats import *

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
