import json
from . import BasicSerializer


class JsonSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        return json.dumps(data)

    @staticmethod
    def deserialize(data):
        return json.loads(data)

