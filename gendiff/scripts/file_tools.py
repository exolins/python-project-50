# file_read
import json
import sys

import yaml

YAML = (".yml", ".yaml")
JSON = (".json", ".jsn")


def read_yaml(file_path):
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


def read_json(file_path):
    return json.load(open(file_path))


def read_file(file_path):
    if file_path.endswith(YAML):
        return read_yaml(file_path)
    if file_path.endswith(JSON):
        return read_json(file_path)
