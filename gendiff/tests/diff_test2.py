# diff_test
# from pathlib import Path

# from gendiff.gendiff import *
from gendiff.genfunc import *

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


def test_file_diff_new():
    file1 = read_file(file_path_json_1)
    file2 = read_file(file_path_json_2)
    file_nested = read_file(file_path_nested_json_1)
    file_nested2 = read_file(file_path_nested_json_2)
    tree = make_tree(file_nested)
    tree2 = make_tree(file_nested2)
    branch1 = get_branches(tree)
    print(tree)
    print("##########tree2")
    print(tree2)
    print("##########branch")
    print(list(branch1))

    assert tree == {}
