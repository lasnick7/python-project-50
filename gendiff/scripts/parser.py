import json

# file1_parsed = parse("tests/fixtures/file1.json")
# file2_parsed = parse("tests/fixtures/file2.json")
def parse(path):
    res = json.load(open(path))
    # print(res)
    return res
