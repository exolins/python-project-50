from .scripts.gendiff import generate_diff
from .source.arg_parser import parse_sh_args
from .source.diff import diff, json_view, plain_view, stylish_view
from .source.file_read import read_file

__all__ = [
    "diff",
    "generate_diff",
    "stylish_view",
    "plain_view",
    "json_view",
    "read_file",
    "parse_sh_args",
]
