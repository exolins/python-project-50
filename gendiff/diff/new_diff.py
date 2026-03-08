# new version
import itertools
from collections import namedtuple

Node = namedtuple("Node", ("old_value", "new_value"))
Branch = namedtuple("Branch", ("childrens"))


dict1 = {"noob": 123, "node2": 1234, "tree": {"node": 123, "option": 444}}
dict2 = {"noob": 143, "node2": 1234, "tree": {"node": 123, "option": 444}}


def old_value(data: list):
    return data[0]


def new_value(data: list):
    return data[1]


def is_same_value(value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        return True
    if value1 == value2:
        return True
    return False


def diff(dict1: dict, dict2: dict):
    keys = dict1.keys() | dict2.keys()
    result = {}
    for key in keys:
        first = dict1.get(key)
        second = dict2.get(key)
        if isinstance(first, dict) and isinstance(second, dict):
            result[key] = diff(first, second)
        else:
            result[key] = Node(first, second)
    return result


def stylish(value, replacer=" ", spaces_count=1):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_intent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, values in current_value.items():
            old = old_value(values)
            new = new_value(values)
            if is_same_value(old, new):
                lines.append(f"{deep_indent}   {key}: iter_()")
