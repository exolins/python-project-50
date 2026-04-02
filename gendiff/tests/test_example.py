# test_example.py
from typing import namedtuple

import pytest

DiffDict = namedtuple(
    "DiffDict",
    (
        "has_first_value",
        "has_second_value",
        "first_is_dict",
        "second_is_dict",
        "first_value",
        "second_value",
        "childrens",
    ),
)


# data1 = {"key1": "value1"}
# data2 = {"key1": "value2"}
# data_result = {"key1": (True, True, "value1", "value2", "updated", {})}
def make_diff_dict(key, data1, data2):
    result = DiffDict()
    result.has_first_value = key in data1
    result.has_second_value = key in data2
    result.first_is_dict = isinstance(data1.get(key), dict)
    result.second_is_dict = isinstance(data2.get(key), dict)
    if result.fitst_is_dict
    
def make_result(key, data1, data2):
    flag1 = key in data1
    flag2 = key in data2
    value1 = data1.get(key)
    value2 = data2.get(key)
    match flag1, flag2:
        case True, True:
            if value1 == value2:
                status = "unchanged"
            else:
                status = "updated"
        case True, False:
            status = "removed"
        case False, True:
            status = "added"
    return (flag1, flag2, value1, value2, status, {})


def diff(data1, data2):
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        result[key] = make_result(key, data1, data2)
    return result


@pytest.mark.parametrize(
    "data1, data2, data_result",
    [
        (
            {"key1": "value1"},
            {"key1": "new_value1"},
            """
            {
                - key1: 'value1'
                + key1: 'new_value1'
            }
            
            """,
        ),
        (
            {"key1": "value1"},
            {"key1": "value1"},
            """
            {
                  key1: 'value1'
            }
            
            """,
        ),
    ],
)
def test_plain(data1, data2, data_result):
    assert plain(diff(data1, data2)) == data_result


@pytest.mark.parametrize(
    "data1, data2, data_result",
    [
        (
            {"key1": "value1"},
            {"key1": "new_value1"},
            {"key1": (True, True, "value1", "new_value1", "updated", {})},
        ),
        (
            {"key1": "value1"},
            {"key1": "value1"},
            {"key1": (True, True, "value1", "value1", "unchanged", {})},
        ),
        (
            {"key1": "value1"},
            {},
            {"key1": (True, False, "value1", None, "removed", {})},
        ),
        (
            {"key1": "value1"},
            {"key1": {"nested": "nested_val"}},
            {
                "key1": (
                    True,
                    True,
                    "value1",
                    {"nested": "nested_value"},
                    "unchanged",
                    {"nested": (False, True, None, "nested_value", "added", {})},
                )
            },
        ),
    ],
)
def test_diff(data1, data2, data_result):
    assert diff(data1, data2) == data_result
