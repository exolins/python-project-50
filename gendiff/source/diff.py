import itertools
import json


def stylish_view(value, replacer=" ", spaces_count=1):
    def iter_(current_value, depth, node_type):
        if not isinstance(current_value, dict):
            return current_value

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        if not node_type:
            for key, value_inner in current_value.items():
                lines.append(
                    f"{deep_indent} {key}: {iter_(value_inner, deep_indent_size, False)}"
                )
        else:
            for key, value_inner in sorted(current_value.items()):
                if value_inner["type"] == "option":
                    match value_inner["status"]:
                        case "added":
                            lines.append(
                                f"{deep_indent} + {key}: {iter_(value_inner['value'], deep_indent_size, False)}"
                            )
                        case "removed":
                            lines.append(
                                f"{deep_indent} - {key}: {iter_(value_inner['value'], deep_indent_size, False)}"
                            )
                        case "updated":
                            lines.append(
                                f"{deep_indent} - {key}: {iter_(value_inner['old_value'], deep_indent_size, False)}"
                            )
                            lines.append(
                                f"{deep_indent} + {key}: {iter_(value_inner['new_value'], deep_indent_size, False)}"
                            )
                        case "same":
                            lines.append(
                                f"{deep_indent}   {key}: {iter_(value_inner['value'], deep_indent_size, False)}"
                            )
                else:
                    lines.append(
                        f"{deep_indent} {key}: {iter_(value_inner['childrens'], deep_indent_size, True)}"
                    )

        result = itertools.chain("{", lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(value, 0, True)


def diff(dict1, dict2):
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
                "childrens": diff(dict1[key], dict2[key]),
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


# def main():
#     print("Hello from sample-proj!")


# if __name__ == "__main__":
#     main()


def return_complex_or_value(value):
    return "[complex value]" if isinstance(value, dict) else f"'{value}'"


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
                        f"Property {full_name} was added with value: {return_complex_or_value(value_inner['value'])}"
                    )
                case "updated":
                    lines.append(
                        f"Property {full_name} was updated. From {return_complex_or_value(value_inner['old_value'])} to {return_complex_or_value(value_inner['new_value'])}"
                    )
        else:
            lines.append(plain_view(value_inner["childrens"], full_name))
    return "\n".join(lines)


def json_view(diff_value):
    return json.dumps(diff_value, indent=4)
