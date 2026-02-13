# diff_test
from pathlib import Path

from gendiff.gendiff import *

# from gendiff.gendiff import make_tree
from gendiff.file_read import read_file

from gendiff.gendiff import Node


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def gendiff(dict1, dict2, format):
    match format:
        case "plain":
            return diff(dict1, dict2).plain()
        case "stylish":
            return diff(dict1, dict2).slylish()


def diff_test():
    dict1 = {"option1": "value1"}
    dict2 = {"option1": "value2"}
    assert diff(dict1, dict2) == []


def note_test():
    node = Node("key1", NEW, "old1", "new1")
    assert node == resulte


dict1 = {"option1": "value1"}
dict2 = {"option1": "value2"}
result_plain = "Property 'option' was updated. From 'value1' to 'value2'"

result_stylish = """
    - option1: 'value1'
    + option1: 'value2'
"""

dict11 = {
    "opt1": "value1",
    "opt2": "value2",
    "opt3": {"nest1": "nest_val1", "nest2": "nest_val2"},
}
dict21 = {"opt1": "value1_new", "opt4": "value4", "opt3": "value_str"}
result_plain2 = """
    Property 'opt1' was updated. From 'value1' to 'value2'
    Property 'opt2' was removed.
    Property 'opt3' was updated. From [complex value] to 'value_str'
    Property 'opt4 was added with value: 'value4' 
"""
result_stylish2 = """
    - opt1: 'value1'
    + opt1: 'value2'
    - opt2: 'value2'
    - opt3: {
        nest1: 'nest_val1'
        nest2: 'nest_val1'
    }
    + opt3: 'value_str'
    + opt4: 'value4'
"""


def first_test():
    assert generate_diff(file1, file2, "stylish") == stylish_result
    assert generate_diff(file1, file2, "flat") == flat_result
