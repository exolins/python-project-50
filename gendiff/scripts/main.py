from gendiff import (
    json_view,
    make_diff,
    parse_sh_args,
    plain_view,
    read_file,
    stylish_view,
)

#


def generate_diff(file1, file2, format="stylish"):
    file1 = read_file(file1)
    file2 = read_file(file2)

    try:
        result = make_diff(file1, file2)

    except Exception as e:
        return "something wrong with make_diff"

    match format:
        case "stylish":
            return stylish_view(result)
        case "plain":
            return plain_view(result)
        case "json":
            return json_view(result)
        case _:
            return f"'{format}' is unknown format of output"


def main():
    args = parse_sh_args()
    first_file = args.first_file
    second_file = args.second_file

    format = args.format
    return generate_diff(first_file, second_file, format)
