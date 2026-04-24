
from gendiff.formatters.json_format import json_view
from gendiff.formatters.plain import plain_view
from gendiff.formatters.stylish import stylish_view
from gendiff.scripts.file_tools import read_file
from gendiff.scripts.make_diff import make_diff


def generate_diff(file1, file2, format="stylish"):
    file1 = read_file(file1)
    file2 = read_file(file2)

    try:
        result = make_diff(file1, file2)

    except Exception:
        return "something wrong with make_diff"

    match format:
        case "stylish":
            return stylish_view(result)
        case "plain":
            return plain_view(result)
        case "json":
            return json_view(result)
        case _:
            return f"'{format}' is unknown format of output"
