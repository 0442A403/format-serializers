import argparse
from server import start_server
from proxy_server import start_proxy_server
from __init__ import *

if __name__ == '__main__':
    if args.target == "serializer":
        assert DATA_FORMAT is not None
        port = os.getenv(DATA_FORMAT.upper())
        assert port is not None
        start_server(DATA_FORMAT, port)
    else:
        port = os.getenv("PROXY")
        assert port is not None
        start_proxy_server(port)

