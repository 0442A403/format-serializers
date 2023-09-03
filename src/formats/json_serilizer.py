import json

from . import BasicSerializer


class JsonSerializer(BasicSerializer):
    addr = "http://127.0.0.1:5000"

    @staticmethod
    def serialize(data):
        return json.loads(data)

    @staticmethod
    def deserialize(data):
        return json.dumps(data)
