class SerializerSettings:
    def __init__(self, host, port, data_format):
        self.host = host
        self.port = port
        self.addr = f"http://{host}:{port}"
        self.data_format = data_format
