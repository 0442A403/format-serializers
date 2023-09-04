class SerializerSettings:
    def __init__(self, port):
        self.data_format = 'json'
        self.port = port
        self.addr = f"http://127.0.0.1:{port}"
