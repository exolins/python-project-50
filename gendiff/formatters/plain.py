
from types import NoneType


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
