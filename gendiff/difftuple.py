from collections import namedtuple

Node = namedtuple("Node", "name, value, version")

Branch = namedtuple("Branch", "name, version, children")


class Tree:
    def __init__(self, **items):
        self._childrens = [items]

    def __repr__(self):
        return f"Tree({self._childrens})"

    def __len__(self):
        return len(self._childrens)

    def __getitem__(self, position):
        return self._childrens[position]


# def make_tree(data):
#     for key, value in data.items():
#         if isinstance(value, dict):
#             return Branch(key, 'origin', make_tree(value))
def make_tree(data):
    result = []
    for key, value in data.items():
        match value:
            case dict(value):
                result.append(Branch(key, "old", make_tree(value)))
            case _:
                result.append(Node(key, value, "old"))
    return result
