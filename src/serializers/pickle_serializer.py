import pickle
from . import BasicSerializer


class PickleSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        return pickle.dumps(data)

    @staticmethod
    def deserialize(data, already_binary=False):
        if already_binary:
            binary = data
        else:
            binary = bytes(map(ord, data))
        return pickle.loads(binary)
