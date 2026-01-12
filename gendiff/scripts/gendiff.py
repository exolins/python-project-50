import argparse
import json
def read_json(file_path):
    return json.load(open(file_path))
# def file_get():
#     file = read_json('gendiff')
def main():
    print("Hello from python-project-50!")

    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.',
                    epilog='Text at the bottom of help')
    parser.add_argument("-f","--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(args)
    print(args.first_file)
    first_file = args.first_file
    second_file = args.second_file
    file1 = read_json(first_file)
    file2 = read_json(second_file)
    for col in file1:
        print(col)
    print(file1, file2)
    

