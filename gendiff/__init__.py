from .source.diff import stylish_view, plain_view, diff, json_view
from .source.file_read import read_file
from .source.arg_parser import parse_sh_args
from .scripts.gendiff import generate_diff

__all__ = [
    "diff",
    "generate_diff",
    "stylish_view",
    "plain_view",
    "json_view",
    "read_file",
    "parse_sh_args",
]
