class BasicSerializer:
    addr = None

    @staticmethod
    def serialize(data):
        raise NotImplementedError("NOT IMPLEMENTED")

    @staticmethod
    def deserialize(data):
        raise NotImplementedError("NOT IMPLEMENTED")
