import pickle
import json
from . import BasicSerializer


class PickleSerializer(BasicSerializer):
    addr = "http://localhost:5000"

    @staticmethod
    def serialize(data):
        return pickle.dumps(data)

    @staticmethod
    def deserialize(data):
        binary_data = bytes(map(ord, data))
        return pickle.loads(binary_data)
