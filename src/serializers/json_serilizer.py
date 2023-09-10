import json
from . import BasicSerializer


class JsonSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        return json.dumps(data)

    @staticmethod
    def deserialize(data, already_binary=False):
        return json.loads(data)

