from .. import BasicSerializer
from io import BytesIO
import fastavro
import pathlib
import json


path = pathlib.Path(__file__).parent.resolve()
with open(path.joinpath("message.avro")) as file:
    SCHEMA = json.loads(file.read())


class AvroSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        bytes_writer = BytesIO()
        fastavro.schemaless_writer(bytes_writer, SCHEMA, data)
        return bytes_writer.getvalue()

    @staticmethod
    def deserialize(data):
        binary = bytes(map(ord, data))

        bytes_writer = BytesIO()
        bytes_writer.write(binary)
        bytes_writer.seek(0)

        return fastavro.schemaless_reader(bytes_writer, SCHEMA)
