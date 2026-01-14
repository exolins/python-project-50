# diff_test
from pathlib import Path

from gendiff.gendiff import generate_diff, read_json


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


result_from = '''- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
+ timeout: 20
- timeout: 50
+ verbose: True'''


def read_file(filename):
    return get_test_data_path(filename).read_text()


# def write_file():
#     out = open(get_test_data_path('result.txt'), 'w')

#     file1 = get_test_data_path('file1.json')
#     file2 = get_test_data_path('file2.json')
#     file1 = read_json(file1)
#     file2 = read_json(file2)
#     # expected = read_file('result.txt')
#     actual = generate_diff(file1, file2)
#     out.write(actual)
#     out.close()
    
# def test_write():
#     write_file()

    
def test_file_diff():
    file1 = get_test_data_path('file1.json')
    file2 = get_test_data_path('file2.json')
    file1 = read_json(file1)
    file2 = read_json(file2)
    expected = read_file('result.txt')
    actual = generate_diff(file1, file2)
    assert actual == result_from
    assert actual == expected



