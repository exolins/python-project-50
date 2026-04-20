import itertools
import json
from types import NoneType


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


# def stylish_line(indent_string, symbol, key, value):
#     result = [indent_string, symbol, key, ": ", value]
#     result.append(indent_string)
#     result.append(symbol)
#     result.append(key)
#     result.append(": ")
#     result.append(value)
#     return "".join([str[x] for x in result])


def stylish_view(value, replacer=" ", spaces_count=4):
    def i_(current_value, depth, node_type):
        if not isinstance(current_value, dict):
            return bool_hook(current_value)

        deep_indent_size = depth * spaces_count
        d_i = replacer * deep_indent_size
        c_i = replacer * (depth - 1) * spaces_count
        lines = []
        if not node_type:
            for key, val in current_value.items():
                lines.append(f"{d_i}{key}: {i_(val, depth + 1, False)}")
        else:
            for key, val in sorted(current_value.items()):
                if val["type"] == "node":
                    lines.append(
                        "%s  %s: %s"
                        % (
                            d_i[:-2],
                            key,
                            i_(get_val(val, "childrens"), depth + 1, True),
                        )
                    )
                elif val["status"] == "added":
                    lines.append(
                        "%s+ %s: %s"
                        % (
                            d_i[:-2],
                            key,
                            i_(get_val(val, "value"), depth + 1, False),
                        )
                    )

                elif val["status"] == "removed":
                    lines.append(
                        "%s- %s: %s"
                        % (
                            d_i[:-2],
                            key,
                            i_(get_val(val, "value"), depth + 1, False),
                        )
                    )
                elif val["status"] == "updated":
                    lines.append(
                        "%s- %s: %s"
                        % (
                            d_i[:-2],
                            key,
                            i_(
                                get_val(val, "old_value"),
                                depth + 1,
                                False,
                            ),
                        )
                    )
                    lines.append(
                        "%s+ %s: %s"
                        % (
                            d_i[:-2],
                            key,
                            i_(
                                get_val(val, "new_value"),
                                depth + 1,
                                False,
                            ),
                        )
                    )
                else:
                    lines.append(
                        "%s  %s: %s"
                        % (
                            d_i[:-2],
                            key,
                            i_(get_val(val, "value"), depth + 1, False),
                        )
                    )

        result = itertools.chain("{", lines, [c_i + "}"])
        return "\n".join(result)

    return i_(value, 1, True)


def make_diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    result = {}
    for key in keys:
        if key not in dict1:
            result[key] = {
                "type": "option",
                "status": "added",
                "value": dict2[key],
            }
        elif key not in dict2:
            result[key] = {
                "type": "option",
                "status": "removed",
                "value": dict1[key],
            }
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
            result[key] = {
                "type": "option",
                "status": "same",
                "value": dict1[key],
            }

    return result


def plain_hook(data):
    if isinstance(data, bool):
        return "true" if data else "false"
    if isinstance(data, NoneType):
        return "null"
    if isinstance(data, str):
        return "'" + data + "'"
    return data


def complex_val(value):
    return (
        "[complex value]" if isinstance(value, dict) else f"{plain_hook(value)}"
    )


def plain_view(diff_value, parent=""):
    lines = []
    parent_string = "" if parent == "" else parent + "."
    for key, value_inner in sorted(diff_value.items()):
        full_name = f"{parent_string}{key}"
        if value_inner["type"] == "option":
            # print(full_name)
            match value_inner["status"]:
                case "removed":
                    lines.append(f"Property '{full_name}' was removed")
                case "added":
                    lines.append(
                        "Property '%s' was added with value: %s"
                        % (full_name, complex_val(value_inner["value"]))
                    )
                case "updated":
                    lines.append(
                        "Property '%s' was updated. From %s to %s"
                        % (
                            full_name,
                            complex_val(value_inner["old_value"]),
                            complex_val(value_inner["new_value"]),
                        ),
                    )
        else:
            lines.append(plain_view(value_inner["childrens"], full_name))
    return "\n".join(lines)


def json_view(diff_value):
    return json.dumps(diff_value, indent=4)
