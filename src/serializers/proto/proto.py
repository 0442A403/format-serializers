from .. import BasicSerializer
from .Message_pb2 import Message
import json
from google.protobuf import json_format

class ProtoSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        msg = Message()
        json_format.ParseDict(data, msg)
        return msg.SerializeToString()

    @staticmethod
    def deserialize(data):
        msg = Message()
        binary_str = bytes(map(ord, data))
        msg.ParseFromString(binary_str)
        return json_format.MessageToDict(msg)
