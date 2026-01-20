# gendiff main module

# from gendiff.json_loader import read_json


def generate_diff(dic1, dic2):
    set1 = set(dic1.items())
    set2 = set(dic2.items())
    common = set1 & set2
    removed = set1 - set2
    added = set2 - set1
    result = (
        {f"+ {k}": v for (k, v) in added}
        | {f"- {k}": v for (k, v) in removed}
        | {f"  {k}": v for (k, v) in common}
    )
    list_result = list(result.items())
    list_result.sort(key=lambda item: item[0][2:])

    string_list = [str(f"{item[0]}: {item[1]}") for item in list_result]
    # return sorted(list_result, key=lambda item: item[0][3:])
    # return result
    return "\n".join(string_list)


def is_node(item):
    if not isinstance(item, dict):
        return False
    if item.get("type", "") == "dict":
        return True
    return False


def flat_diff(dic1, dic2):
    result = dic1.copy()
    for key in dic2:
        result[key] = result.get(key, {}) | dic2[key]
    return result


def get_version(item):
    return item.get("version", 0)


def get_value(item):
    return item.get("value", "")


def get_childrens(item):
    return item.get("childrens", {})


def merge_diff(dic1, dic2):
    result = {}

    def iter_(item1, item2):
        if is_node(item1) and is_node(item2):
            return {
                "version": -1,
                "childrens": merge_diff(
                    get_childrens(item1), get_childrens(item2)
                ),
            }
        return [item1, item2]

    result = dic1.copy()
    for key in dic2:
        result[key] = iter_(result.get(key, ""), dic2[key])
    return result


# def new_diff(dic1, dic2):
#     nodes1 = filter(is_node, dic1)
#     nodes2 = filter(is_node, dic2)
#     keys = nodes1.keys() | nodes2.keys()
#     for key in keys:
#         result = nodes
#     result = {}
#     for key in leaves2:
#         result[key] = result.get(key, {}) | leaves1[key]


def make_tree(data, version):
    result = {}

    def iter_(value):
        if isinstance(value, dict):
            return {
                "version": version,
                "childrens": make_tree(value, version),
            }
        return {"version": version, "value": value}

    for key, value in data.items():
        result[key] = iter_(value)
    return result


# def generate_diff_old(file1, file2):
#     result = []
#     for k in file1:
#         if k in file2:
#             if file2[k] == file1[k]:
#                 result.append([" ", k, file1[k]])
#             else:
#                 result.append(["-", k, file1[k]])
#                 result.append(["+", k, file2[k]])
#         else:
#             result.append(["-", k, file1[k]])
#     sorted_list = sorted(result, key=lambda key: key[1])
#     string_list = [str(item) for item in sorted_list]
#     # print('\n'.join(string_list))
#     # print(result)
#     return "\n".join(string_list)


# def file_get():
#     file = read_json('gendiff')
# class Diff:
#     def __init__(self, key, value, status):
#         self.key = key
#         self.value = value
#         self.status = status
#     def __repr__(self):
#         return repr((self.key, self.value, self.status))
#     def __str__(self):
#         return f'{self.status} {self.key} {self.value}'
#     def __contains__(self, val):
#         return self.key == val


# def main():

#     args = parse_sh_args()
#     # print(args)

#     # print(args.first_file)
#     first_file = args.first_file
#     second_file = args.second_file
#     file1 = read_json(first_file)
#     file2 = read_json(second_file)
#     # for col in file1:
#     #     print(col)
#     # print(file1, file2)

#     result = []
