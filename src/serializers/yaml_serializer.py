import yaml
from . import BasicSerializer


class YamlSerializer(BasicSerializer):
    @staticmethod
    def serialize(data):
        return yaml.dump(data)

    @staticmethod
    def deserialize(data, already_binary=False):
        return yaml.load(data, Loader=yaml.CLoader)

