import pickle
from . import BasicSerializer


class PickleSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        return pickle.dumps(data)

    @staticmethod
    def deserialize(data):
        binary = bytes(map(ord, data))
        return pickle.loads(binary)
