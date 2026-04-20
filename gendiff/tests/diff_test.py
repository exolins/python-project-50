import pytest

# from gendiff.source.file_tools import read_file
from gendiff import generate_diff
from gendiff.source.main_diff import make_diff


def read_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()


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
        "two": {
            "type": "option",
            "status": "removed",
            "value": {"nested": "value1"},
        },
        "lol": {"type": "option", "status": "added", "value": "value2"},
        "new": {
            "type": "option",
            "status": "added",
            "value": {"nested": "value2"},
        },
    },
)


@pytest.mark.parametrize(
    "data1, data2, data_result",
    [param1, param2, param3, param4, param5, param6, param7],
)
def test_diff(data1, data2, data_result):
    assert make_diff(data1, data2) == data_result


@pytest.mark.parametrize(
    "file_path1, file_path2, expected_result",
    [
        (
            "gendiff/tests/test_data/file1.json",
            "gendiff/tests/test_data/file2.json",
            "gendiff/tests/test_data/expected_result_json.txt",
        ),
        (
            "gendiff/tests/test_data/file1.yaml",
            "gendiff/tests/test_data/file2.yaml",
            "gendiff/tests/test_data/expected_result_yaml.txt",
        ),
    ],
)
def test_generate_diff(file_path1, file_path2, expected_result):
    diff = generate_diff(file_path1, file_path2)
    expected = read_file(expected_result).strip()
    assert diff.strip() == expected


@pytest.mark.parametrize(
    "file_path1, file_path2, expected_result",
    [
        (
            "gendiff/tests/test_data/file1.json",
            "gendiff/tests/test_data/file2.json",
            "gendiff/tests/test_data/expected_result_plain.txt",
        ),
        (
            "gendiff/tests/test_data/file1.yaml",
            "gendiff/tests/test_data/file2.yaml",
            "gendiff/tests/test_data/expected_result_plain.txt",
        ),
    ],
)
def test_generate_diff_plain(file_path1, file_path2, expected_result):
    diff = generate_diff(file_path1, file_path2, format="plain")
    expected = read_file(expected_result).strip()
    assert diff.strip() == expected


@pytest.mark.parametrize(
    "file_path1, file_path2, expected_result",
    [
        (
            "gendiff/tests/test_data/file1.json",
            "gendiff/tests/test_data/file2.json",
            "gendiff/tests/test_data/expected_result_json_format.txt",
        ),
        (
            "gendiff/tests/test_data/file1.yaml",
            "gendiff/tests/test_data/file2.yaml",
            "gendiff/tests/test_data/expected_result_json_format.txt",
        ),
    ],
)
def test_generate_diff_json(file_path1, file_path2, expected_result):
    diff = generate_diff(file_path1, file_path2, format="json")
    expected = read_file(expected_result).strip()
    assert diff.strip() == expected
