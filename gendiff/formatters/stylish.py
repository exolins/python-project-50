import itertools
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
