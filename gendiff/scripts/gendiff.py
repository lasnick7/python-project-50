import argparse
from gendiff.scripts.find_difference import find_diff
from gendiff.scripts.parser import parse
from gendiff.formatters.formatter1 import format

def generate_diff(file_path1, file_path2):
    file1_parsed = parse(file_path1)
    file2_parsed = parse(file_path2)
    diff = find_diff(file1_parsed, file2_parsed)
    return format(diff)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', metavar='FORMAT', help="set format of output")
    parser.parse_args()


if __name__ == "__main__":
    # main()
    print(generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json"))
