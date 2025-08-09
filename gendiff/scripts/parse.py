import json

def parse(path):
    res = json.load(open(path))
    print(res)
    return res

parse("../../tests/fixtures/file1.json")