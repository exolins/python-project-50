from .source.arg_parser import parse_sh_args
from .source.file_tools import read_file
from .source.main_diff import json_view, make_diff, plain_view, stylish_view
from .scripts.main import generate_diff

__all__ = [
    "make_diff",
    "generate_diff",
    "stylish_view",
    "plain_view",
    "json_view",
    "read_file",
    "parse_sh_args",
]
