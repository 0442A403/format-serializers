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
    def deserialize(data, already_binary=False):
        msg = Message()
        if already_binary:
            binary = data
        else:
            binary = bytes(map(ord, data))
        msg.ParseFromString(binary)
        return json_format.MessageToDict(msg)
