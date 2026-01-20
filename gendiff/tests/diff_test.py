# diff_test
# from pathlib import Path

from gendiff.gendiff import *

# from gendiff.gendiff import make_tree
from gendiff.file_read import read_file

file_path_result = "gendiff/tests/test_data/result.txt"
file_path_json_1 = "gendiff/tests/test_data/file1.json"
file_path_yaml_1 = "gendiff/tests/test_data/file1.yaml"
file_path_json_2 = "gendiff/tests/test_data/file2.json"
file_path_yaml_2 = "gendiff/tests/test_data/file2.yaml"
file_path_nested_json_1 = "gendiff/tests/test_data/nested_file1.json"
file_path_nested_json_2 = "gendiff/tests/test_data/nested_file2.json"

result_from = """- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
+ timeout: 20
- timeout: 50
+ verbose: True"""


def test_file_diff_json():
    file1 = read_file(file_path_json_1)
    file2 = read_file(file_path_json_2)
    file_nested = read_file(file_path_nested_json_1)
    file_nested2 = read_file(file_path_nested_json_2)
    expected = open(file_path_result).read()
    # actual = generate_diff(file1, file2)
    test_tree = make_tree(file_nested, 1)

    test_tree2 = make_tree(file_nested2, 2)

    print("#########TEST############")
    print(test_tree)
    res_merge = merge_diff(test_tree, test_tree2)
    print("###############mege")
    print(list(res_merge))

    nodes1 = filter(is_node, test_tree)
    print(list(nodes1))
    assert test_tree == "123"

    # assert actual == result_from
    # assert actual == expected


def test_file_diff_yaml():
    file1 = read_file(file_path_yaml_1)
    file2 = read_file(file_path_yaml_2)
    expected = open(file_path_result).read()
    actual = generate_diff(file1, file2)
    assert actual == result_from
    assert actual == expected


# def write_file():

#     out = open(get_test_data_path('result.txt'), 'w')

#     file1 = get_test_data_path('file1.json')
#     file2 = get_test_data_path('file2.json')
#     file1 = read_file(file1)
#     file2 = read_file(file2)
#     # expected = read_file('result.txt')
#     actual = generate_diff(file1, file2)
#     out.write(actual)
#     out.close()

# def test_write():
#     write_file()


# def get_test_data_path(filename):
#     return Path(__file__).parent / "test_data" / filename


# def read_file_as_is(filename):
#     return get_test_data_path(filename).read_text(
