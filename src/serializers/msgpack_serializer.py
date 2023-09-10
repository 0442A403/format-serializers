from . import BasicSerializer
import msgpack


class MsgpackSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        return msgpack.packb(data)

    @staticmethod
    def deserialize(data, already_binary=False):
        if already_binary:
            binary = data
        else:
            binary = bytes(map(ord, data))
        return msgpack.unpackb(binary)
