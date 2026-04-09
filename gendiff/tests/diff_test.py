import pytest
from gendiff import diff

# from gendiff.diff import *

REM = "rem"
ADD = "add"
SAME = "same"
UPD = "upd"
NEST = "nest"
param1 = ({}, {}, {})
param2 = ({"one": "value1"}, {"one": "value1"}, {"one": (SAME, "value1")})

param3 = ({"one": "value1"}, {"one": "value2"}, {"one": (UPD, "value1", "value2")})


param4 = (
    {"one": "value1"},
    {"two": "value2"},
    {"one": (REM, "value1"), "two": (ADD, "value2")},
)

param5 = (
    {"one": "value1", "two": {"nested": "value1"}},
    {"one": "value2", "two": {"nested": "value2"}},
    {
        "one": (UPD, "value1", "value2"),
        "two": (NEST, {"nested": (UPD, "value1", "value2")}),
    },
)
param6 = (
    {"one": "value1", "two": {"nested": "value1"}},
    {"one": "value2", "two": "notnested"},
    {"one": (UPD, "value1", "value2"), "two": (UPD, {"nested": "value1"}, "notnested")},
)
param7 = (
    {"one": "value1", "two": {"nested": "value1"}},
    {"lol": "value2", "new": {"nested": "value2"}},
    {
        "one": (REM, "value1"),
        "two": (REM, {"nested": "value1"}),
        "lol": (ADD, "value2"),
        "new": (ADD, {"nested": "value2"}),
    },
)


@pytest.mark.parametrize(
    "data1, data2, data_result",
    [param1, param2, param3, param4, param5, param6, param7],
)
def test_diff(data1, data2, data_result):
    assert diff(data1, data2) == data_result
