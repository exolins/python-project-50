import pytest

from gendiff import *

param1 = ({}, {}, {})
param2 = (
    {"one": "value1"},
    {"one": "value1"},
    {"one": {"type": "option", "status": "same", "value": "value1"}},
)

param3 = (
    {"one": "value1"},
    {"one": "value2"},
    {
        "one": {
            "type": "option",
            "status": "updated",
            "old_value": "value1",
            "new_value": "value2",
        }
    },
)


param4 = (
    {"one": "value1"},
    {"two": "value2"},
    {
        "one": {"type": "option", "status": "removed", "value": "value1"},
        "two": {"type": "option", "status": "added", "value": "value2"},
    },
)

param5 = (
    {"one": "value1", "two": {"nested": "value1"}},
    {"one": "value2", "two": {"nested": "value2"}},
    {
        "one": {
            "type": "option",
            "status": "updated",
            "old_value": "value1",
            "new_value": "value2",
        },
        "two": {
            "type": "node",
            "childrens": {
                "nested": {
                    "type": "option",
                    "status": "updated",
                    "old_value": "value1",
                    "new_value": "value2",
                }
            },
        },
    },
)
param6 = (
    {"one": "value1", "two": {"nested": "value1"}},
    {"one": "value2", "two": "notnested"},
    {
        "one": {
            "type": "option",
            "status": "updated",
            "old_value": "value1",
            "new_value": "value2",
        },
        "two": {
            "type": "option",
            "status": "updated",
            "old_value": {"nested": "value1"},
            "new_value": "notnested",
        },
    },
)
param7 = (
    {"one": "value1", "two": {"nested": "value1"}},
    {"lol": "value2", "new": {"nested": "value2"}},
    {
        "one": {"type": "option", "status": "removed", "value": "value1"},
        "two": {"type": "option", "status": "removed", "value": {"nested": "value1"}},
        "lol": {"type": "option", "status": "added", "value": "value2"},
        "new": {"type": "option", "status": "added", "value": {"nested": "value2"}},
    },
)


@pytest.mark.parametrize(
    "data1, data2, data_result",
    [param1, param2, param3, param4, param5, param6, param7],
)
def test_diff(data1, data2, data_result):
    assert generate_diff(data1, data2) == data_result
