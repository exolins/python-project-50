from gendiff import *
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
    format = args.format
    match format:
        case "stylish":
            return stylish_view(result)
        case "plain":
            return plain_view(result)
        case "json":
            return json_view(result)
        case _:
            return f"'{format}' is unknown format of output"
    # result_view = plain_view(result)
    # print(result)
    # return result_view
