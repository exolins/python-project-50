import inspect
from collections import namedtuple
# from typing import List, Union, Dict

# JsonDict = Dict[Union[JsonDict, str]]

dict1 = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {"key": "value", "doge": {"wow": ""}},
    },
    "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
    "group2": {"abc": 12345, "deep": {"id": 45}},
}


dict2 = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": None,
        "setting4": "blah blah",
        "setting5": {"key5": "value5"},
        "setting6": {"key": "value", "ops": "vops", "doge": {"wow": "so much"}},
    },
    "group1": {"foo": "bar", "baz": "bars", "nest": "str"},
    "group3": {"deep": {"id": {"number": 45}}, "fee": 100500},
}

# >>> noob = json.load(open('tests/test_data/nested_file2.json'))


def diff(data1: dict, data2: dict) -> dict:
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            result[key] = diff(value1, value2)
        else:
            if isinstance(value1, dict):
                value1 = diff(value1, value1)
            if isinstance(value2, dict):
                value2 = diff(value2, value2)
            result[key] = (value1, value2)
    return result


def printable_value(value, spaces=1):
    return value
    result = []
    current_spaces = "  " * spaces
    result.append("{")

    if isinstance(value, dict):
        for k, v in value.items():
            if isinstance(v, dict):
                result.append(f"{current_spaces}{k}:{printable_value(v, spaces + 1)}")
            else:
                result.append(f"{current_spaces}{k}: {v}")
    else:
        return value

    result.append(current_spaces + "}")
    return "\n".join(result)


def plain(data: dict, spaces=1):
    current_spaces = "  " * spaces
    end_spaces = "  " * (spaces - 1)
    print("{")
    for key, value in sorted(data.items()):
        if isinstance(value, dict):
            print(f"{current_spaces}  {key}: ", end="")
            plain(value, spaces + 1)
        elif value[0] == value[1]:
            print(f"{current_spaces}  {key}: {printable_value(value[0], spaces)}")
        elif value[0] is None:
            print(f"{current_spaces}+ {key}: {printable_value(value[1], spaces)}")
        elif value[1] is None:
            print(f"{current_spaces}- {key}: {printable_value(value[0], spaces)}")
        else:
            print(f"{current_spaces}+ {key}: {printable_value(value[1], spaces)}")
            print(f"{current_spaces}- {key}: {printable_value(value[0], spaces)}")
    print(end_spaces + "}")


def style(data: dict, parrent_key=""):
    if parrent_key == "":
        st = ""
    else:
g       st = "."
    for key, value in sorted(data.items()):
        if isinstance(value, dict):
            style(value, st + key)
        else:
            first_value = "[complex value]" if isinstance(value[0], dict) else value[0]
            second_value = "[complex value]" if isinstance(value[1], dict) else value[1]
            if first_value is None:
                print(
                    f"Property '{parrent_key}{st}{key}' was added with value:{second_value}"
                )
            elif second_value is None:
                print(f"{parrent_key}{st}{key} was removed")
            else:
                print(
                    f"Property '{parrent_key}{st}{key}' was updated from. From {first_value} to {second_value}"
                )
