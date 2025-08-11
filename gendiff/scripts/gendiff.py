import argparse

from gendiff.formatters.stylish import format_stylish
from gendiff.scripts.find_difference import find_diff
from gendiff.scripts.parser import parse


def generate_diff(file_path1, file_path2, format_name="stylish"):
    file1_parsed = parse(file_path1)
    file2_parsed = parse(file_path2)
    diff = find_diff(file1_parsed, file2_parsed)
    return format_stylish(diff)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help="set format of output",
                        default='stylish', choices=['stylish', 'plain', 'json'])
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    formatter = args.format
    diff = generate_diff(file_path1, file_path2, formatter)
    print(diff)


if __name__ == "__main__":
    main()
    # print(generate_diff("tests/fixtures/nested/file1.json", "tests/fixtures/nested/file2.json"))
    # print(generate_diff("tests/fixtures/non_nested/file1.yml", "tests/fixtures/non_nested/file2.yml"))
    # print(generate_diff("tests/fixtures/non_nested/file1.yaml", "tests/fixtures/non_nested/file2.yaml"))
