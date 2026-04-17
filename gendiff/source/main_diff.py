from types import NoneType
import itertools
import json


def bool_hook(data):
    if isinstance(data, bool):
        return "true" if data else "false"
    if isinstance(data, NoneType):
        return "null"
    return data


def get_val(data, key):
    if key in data:
        return bool_hook(data[key])
    return "ERROR"


def stylish_view(value, replacer=" ", spaces_count=4):
    def i_(current_value, depth, node_type):
        if not isinstance(current_value, dict):
            return current_value

        deep_indent_size = depth * spaces_count - 2
        d_i = replacer * deep_indent_size
        not_node_indent = replacer * depth * spaces_count
        current_indent = replacer * (spaces_count * (depth - 1) - 2)
        lines = []
        if not node_type:
            for key, val in current_value.items():
                lines.append(f"{not_node_indent}{key}: {i_(val, depth + 1, False)}")
        else:
            for key, val in sorted(current_value.items()):
                if val["type"] == "option":
                    match val["status"]:
                        case "added":
                            lines.append(
                                f"{d_i}+ {key}: {i_(get_val(val, 'value'), depth + 1, False)}"
                            )
                        case "removed":
                            lines.append(
                                f"{d_i}- {key}: {i_(get_val(val, 'value'), depth + 1, False)}"
                            )
                        case "updated":
                            lines.append(
                                f"{d_i}- {key}: {i_(get_val(val, 'old_value'), depth + 1, False)}"
                            )
                            lines.append(
                                f"{d_i}+ {key}: {i_(get_val(val, 'new_value'), depth + 1, False)}"
                            )
                        case "same":
                            lines.append(
                                f"{d_i}  {key}: {i_(get_val(val, 'value'), depth + 1, False)}"
                            )
                else:
                    lines.append(
                        f"{d_i}  {key}: {i_(get_val(val, 'childrens'), depth + 1, True)}"
                    )

        result = itertools.chain("{", lines, [current_indent + "  }"])
        return "\n".join(result)

    return i_(value, 1, True)


def make_diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    result = {}
    for key in keys:
        if key not in dict1:
            result[key] = {"type": "option", "status": "added", "value": dict2[key]}
        elif key not in dict2:
            result[key] = {"type": "option", "status": "removed", "value": dict1[key]}
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result[key] = {
                "type": "node",
                "childrens": make_diff(dict1[key], dict2[key]),
            }
        elif dict1[key] != dict2[key]:
            result[key] = {
                "type": "option",
                "status": "updated",
                "old_value": dict1[key],
                "new_value": dict2[key],
            }
        else:
            result[key] = {"type": "option", "status": "same", "value": dict1[key]}

    return result


def complex_val(value):
    return "[complex value]" if isinstance(value, dict) else f"'{bool_hook(value)}'"


def plain_view(diff_value, parent=""):
    lines = []
    parent_string = "" if parent == "" else parent + "."
    for key, value_inner in sorted(diff_value.items()):
        full_name = f"{parent_string}{key}"
        if value_inner["type"] == "option":
            # print(full_name)
            match value_inner["status"]:
                case "removed":
                    lines.append(f"Property {full_name} was removed")
                case "added":
                    lines.append(
                        f"Property {full_name}"
                        + "was added with value: "
                        + f"{complex_val(value_inner['value'])}"
                    )
                case "updated":
                    lines.append(
                        f"Property {full_name} was updated."
                        + f" From {complex_val(value_inner['old_value'])} to {complex_val(value_inner['new_value'])}"
                    )
        else:
            lines.append(plain_view(value_inner["childrens"], full_name))
    return "\n".join(lines)


def json_view(diff_value):
    return json.dumps(diff_value, indent=4)
