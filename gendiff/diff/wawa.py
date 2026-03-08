from collections import namedtuple
from itertools import chain

Option = namedtuple("Option", ("old_value", "new_value"))

dict1 = {"noob": 123, "node2": 1234, "tree": {"node": 123, "option": 444}}
dict2 = {"noob": 143, "node2": 1234, "tree": {"node": 123, "option": 444}}

dict11 = {"noob": 123, "node2": 1234, "tree": {"node": 123, "option": 444}}
dict22 = {
    "noob": 143,
    "node3": 1234,
    "tree": {"node": 123, "option": 44234, "baba": 123123, "inner": {"dudu": 123}},
    "awwa": {123: 123},
}


def is_dict(value):
    return isinstance(value, dict)


def diff_by_key(key, dict1: dict, dict2: dict):
    val1 = dict1.get(key)
    val2 = dict2.get(key)
    if isinstance(val1, dict) and (isinstance(val2, dict)):
        return diff(val1, val2)
    if isinstance(val1, dict):
        return Option(diff(val1, val1), val2)
    if isinstance(val2, dict):
        return Option(val1, diff(val2, val2))
    return Option(val1, val2)

-
def diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    result = {}
    for key in keys:
        result[key] = diff_by_key(key, dict1, dict2)
    return result


def return_complex_or_value(value):
    return "[complex value]" if isinstance(value, dict) else value


def option_plain(value: Option, parent_string="", option_name=""):
    full_name = f"{parent_string}{option_name}"

    old_value = return_complex_or_value(value.old_value)
    new_value = return_complex_or_value(value.new_value)
    if new_value is None:
        return f"Property {full_name} was removed"
    if old_value is None:
        return f"Property {full_name} was added with value: {new_value}"
    if old_value != new_value:
        return f"Property {full_name} was updated. From {old_value} to {new_value}"
    # return f"something {value} val, {option_name} name"


def not_none(x):
    if x is None:
        return False
    return True


def plain_diff(diff_result: dict, parent=""):
    result = []
    parent_string = "" if parent == "" else f"{parent}."
    for option_name, option_value in diff_result.items():
        if isinstance(option_value, Option):
            result.append(option_plain(option_value, parent_string, option_name))

        else:
            result.append(plain_diff(option_value, f"{option_name}"))
            # result = chain(
            #     result,
            #     plain_diff(option_value, f"{parent_string}{option_name}"),
            # )
    # result = sorted(filter(lambda x: not_none(x), result))
    return result
    # return "\n".join(result)


def style_by_line(option_name, value: Option):
    old_value = return_complex_or_value(value.old_value)
    new_value = return_complex_or_value(value.new_value)


STATUS = {"removed": "-", "added": "+", "same": " "}


def style_diff(diff_result: dict):
    result = []
    for option_name, option_value in diff_result.items():
        new_value = option_value.new_value
        old_value = option_value.old_value

        if isinstance(new_value, dict) and isinstance(old_value, dict):
            result.append(style_diff(new_value))
        elif new_value == old_value:
            result.append(f"SAME {option_name} {new_value}")
        else:
            if new_value is not None:
                result.append(f"ADD {option_name} {new_value}")
            if old_value is not None:
                result.append(f"REM {option_name} {new_value}")


res = diff(dict11, dict22)
print(plain_diff(res))
