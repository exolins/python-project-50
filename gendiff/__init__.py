# gendiff/__init__.py
from .scripts.arg_parser import parse_sh_args
from .scripts.diff import generate_diff
from .scripts.make_diff import make_diff

__all__ = ["generate_diff", "parse_sh_args"]
