from server import start_server
from __init__ import SERIALIZERS
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--format",
    choices=SERIALIZERS.keys(),
    type=str,
    required=True,
)

args = parser.parse_args()

format = args.format

if __name__ == '__main__':
    start_server(format)
