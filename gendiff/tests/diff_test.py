import pytest

REM = 0
ADD = 1
SAME = 2
UPD = 3
NEST = 4
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
    {"one": (UPD, "value1", "value2"), "two": (NEST, {"nested": (UPD, "value1", "value2")})},
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


def diff(data1: dict, data2: dict):
    keys = data1.keys() | data2.keys()
    result = {}
    for key in keys:
        flag1 = key in data1
        flag2 = key in data2
        match flag1, flag2:
            case True, False:
                result[key] = (REM, data1[key])
            case False, True:
                result[key] = (ADD, data2[key])
            case True, True:
                if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                    result[key] = (NEST, diff(data1[key], data2[key]))
                else:
                    if data1[key] == data2[key]:
                        result[key] = (SAME, data1[key])
                    else:
                        result[key] = (UPD, data1[key], data2[key])
    return result


@pytest.mark.parametrize(
    "data1, data2, data_result",
    [param1, param2, param3, param4, param5, param6, param7],
)
def test_diff(data1, data2, data_result):
    assert diff(data1, data2) == data_result
