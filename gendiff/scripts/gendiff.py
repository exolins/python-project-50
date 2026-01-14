from gendiff.gendiff import generate_diff, read_json, parse_sh_args


def main():
    # print("Hello from python-project-50!")

    args = parse_sh_args()
    # print(args)

    # print(args.first_file)
    first_file = args.first_file
    second_file = args.second_file
    file1 = read_json(first_file)
    file2 = read_json(second_file)
    result = generate_diff(file1, file2)
    return result
