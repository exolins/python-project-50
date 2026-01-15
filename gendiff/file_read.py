# file_read
from yaml import load, dump
from yaml import Loader, Dumper
import json

YAML = (".yml", ".yaml")
JSON = (".json", ".jsn")


def read_yaml(file_path):
    return load(open(file_path), Loader)


def dump_yaml(data):
    return dump(data, Dumper=Dumper)


def read_json(file_path):
    print(file_path)
    print(open(file_path).read())
    return json.load(open(file_path))


def read_file(file_path):
    if file_path.endswith(YAML):
        return read_yaml(file_path)
    if file_path.endswith(JSON):
        return read_json(file_path)
