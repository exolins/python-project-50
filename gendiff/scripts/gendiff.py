import argparse
def main():
    print("Hello from python-project-50!")

    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.',
                    epilog='Text at the bottom of help')
    parser.add_argument("-f","--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.parse_args()

