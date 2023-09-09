from . import BasicSerializer
import msgpack


class MsgpackSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        return msgpack.packb(data)

    @staticmethod
    def deserialize(data):
        binary_str = bytes(map(ord, data))
        return msgpack.unpackb(binary_str)
