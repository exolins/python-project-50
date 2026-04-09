REM = "rem"
ADD = "add"
SAME = "same"
UPD = "upd"
NEST = "nest"


def diff(data1: dict, data2: dict):
    keys = data1.keys() | data2.keys()
    result = {}
    for key in keys:
        flag1 = key in data1
        flag2 = key in data2
        match flag1, flag2:
            case True, False:
                result[key] = (REM, data1[key])
            case False, True:
                result[key] = (ADD, data2[key])
            case True, True:
                if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                    result[key] = (NEST, diff(data1[key], data2[key]))
                else:
                    if data1[key] == data2[key]:
                        result[key] = (SAME, data1[key])
                    else:
                        result[key] = (UPD, data1[key], data2[key])
    return result


SYMBOL = "."


def style_string(value, indent):
    if isinstance(value, dict):
        result = []
        result.append(f"{SYMBOL * indent} (")
        for key, value in value.items():
            result.append(f"{SYMBOL * indent}  {key}:{style_string(value, indent + 1)}")
        result.append("))))")
        return "\n".join(result)
    return value[1]


def stylish(data, base_indent=0):
    if not data:
        return 0
    result = []
    result.append(base_indent * SYMBOL + "{")
    indent = base_indent + 1
    for key, value in data.items():
        match value[0]:
            case "add":
                result.append(
                    f"{SYMBOL * indent}+ {key}:{style_string(value[1], indent + 1)}"
                )
            case "rem":
                result.append(
                    f"{SYMBOL * indent}- {key}:{style_string(value[1], indent + 1)}"
                )
            case "upd":
                result.append(
                    f"{SYMBOL * indent}+ {key}:{style_string(value[2], indent + 1)}"
                )
                result.append(
                    f"{SYMBOL * indent}- {key}:{style_string(value[1], indent + 1)}"
                )
            case "same":
                result.append(
                    f"{SYMBOL * indent}  {key}:{style_string(value[1], indent + 1)}"
                )
            case "nest":
                result.append(
                    f"{SYMBOL * indent}  {key}:{stylish(value[1], indent + 1)}"
                )
            case _:
                result.append("ERRRROORRR")
    result.append("}")
    print("\n".join(result))


test = {
    "bob": ("add", "noob"),
    "sam": ("rem", "noobs"),
    "upda": ("upd", "val1", "val2"),
}
test_nest = {"first": ("same", "first"), "Nesttest": ("nest", test)}
stylish(test)
stylish(test_nest)
