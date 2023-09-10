class BasicSerializer:
    @staticmethod
    def serialize(data):
        raise NotImplementedError("NOT IMPLEMENTED")

    @staticmethod
    def deserialize(data, already_binary=False):
        raise NotImplementedError("NOT IMPLEMENTED")
