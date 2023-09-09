from . import BasicSerializer
import xmltodict as xml


class XmlSerializer(BasicSerializer):
    ROOT = "root"

    @staticmethod
    def serialize(data):
        return xml.unparse({XmlSerializer.ROOT: data})

    @staticmethod
    def deserialize(data):
        return xml.parse(data)[XmlSerializer.ROOT]
