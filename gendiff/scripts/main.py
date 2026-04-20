from gendiff import generate_diff, parse_sh_args

#


def main():
    args = parse_sh_args()
    first_file = args.first_file
    second_file = args.second_file

    format = args.format
    print(generate_diff(first_file, second_file, format))
