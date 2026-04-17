# file_read
from types import NoneType
import json
import yaml
import sys
# from yaml import Dumper, Loader, dump, load

YAML = (".yml", ".yaml")
JSON = (".json", ".jsn")


# def json_hook(data):
#     for key, val in data.items():
#         if isinstance(val, bool):
#             data[key] = "true" if val else "false"
#         if isinstance(val, NoneType):
#             data[key] = "null"
#     return data


def read_yaml(file_path):
    # return load(open(file_path), Loader)

    try:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
        return data
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"File not found: {e}", file=sys.stderr)
        sys.exit(1)


# def dump_yaml(data):
#     return dump(data, Dumper=Dumper)


def read_json(file_path):
    # print(file_path)
    # print(open(file_path).read())

    return json.load(open(file_path))


def read_file(file_path):
    if file_path.endswith(YAML):
        return read_yaml(file_path)
    if file_path.endswith(JSON):
        return read_json(file_path)
