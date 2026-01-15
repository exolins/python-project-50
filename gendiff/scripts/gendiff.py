from gendiff.gendiff import generate_diff
from gendiff.arg_parser import parse_sh_args
from gendiff.file_read import read_file
# def diff_json():
#


def main():
    # print("Hello from python-project-50!")

    args = parse_sh_args()
    # print(args)

    # print(args.first_file)
    first_file = args.first_file
    second_file = args.second_file

    file1 = read_file(first_file)
    file2 = read_file(second_file)
    result = generate_diff(file1, file2)
    return result
