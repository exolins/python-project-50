def make_leave(node):
    return {"type": "leave", "value": node}


def make_branch(node):
    return {"type": "branch", "childrens": make_tree(node)}


def get_childrens(node):
    return node["childrens"]


def get_leaves(tree):
    return


def is_leave(node):
    return node["type"] == "leave"


def is_branch(node):
    return node["type"] == "branch"


def get_leaves(tree):
    return filter(is_leave, tree)


def get_branches(tree):
    return filter(is_branch, tree.items())


def make_tree(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = make_branch(value)
        else:
            result[key] = make_leave(value)
    return result


def diff(dict1, dict2):
    tree1 = make_tree(dict1)
    tree2 = make_tree(dict2)
