import itertools
from collections import namedtuple

Node = namedtuple("Node", ("key", "marker", "value"))
Branch = namedtuple("Branch", ("key", "marker", "childrens"))


# BEGIN
def stringify(value, replacer=" ", spaces_count=1):
    def iter_(current_value, depth):
        if not isinstance(current_value, list):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for node in current_value:
            lines.append(
                f"{deep_indent}{node.key}{node.marker}: {iter_(node.value, deep_indent_size)}"
            )
        result = itertools.chain("{", lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(value, 0)


# END
#
def booblik():
    noob = {}
    noob["vav"] = "nono"
    print(noob["vav"])


def noob(lol):
    len(lol)


dict1 = {
    "opt1": "123",
    "opt2": "lol",
    "opt3": "lll",
    "dict": {1: 2, 2: 3},
    "dict2": {1: 2},
}
dict2 = {
    "opt1": "113",
    "opt2": "lol",
    "opt3": "lll",
    "dict": {1: 4, 2: 3},
    "CUPUP": {1: 3, "sdt": 123, "sdf": {1: 1234}},
}

retult = {
    ("opt1", "-"): "123",
    ("opt1", "+"): "113",
    ("opt2", " "): "lol",
    ("opt3", " "): "lll",
    ("dict", " "): {(1, "-"): 2},
}


def branch(node):
    result = []
    for key, value in node.items():
        if isinstance(value, dict):
            result.append(Node(key, "", branch(value)))
        else:
            result.append(Node(key, " ", value))
    return result


def diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    result = []
    for key in keys:
        match (dict1.get(key), dict2.get(key)):
            case (dict(first), dict(second)):
                result.append(Node(key, "   ", diff(first, second)))
            case (dict(first), second) if not isinstance(second, dict):
                result.append(Node(key, " - ", branch(first)))
            case (first, dict(second)) if not isinstance(first, dict):
                result.append(Node(key, " + ", branch(second)))
            case (first, second) if first == second:
                result.append(Node(key, "   ", first))
            case (first, second) if first == None:
                result.append(Node(key, " + ", first))
            case (first, second) if second == None:
                result.append(Node(key, " - ", first))
            case (first, second) if first != None and first != second:
                result.append(Node(key, " - ", first))
                result.append(Node(key, " + ", second))
    return result


def main():
    print("Hello from sample-proj!")
    booblik()
    result = diff(dict1, dict2)
    string_result = stringify(result, "--", 3)
    print(string_result)


if __name__ == "__main__":
    main()
