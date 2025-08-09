import json
import os

import yaml

# file1_parsed = parse("tests/fixtures/file1.json")
# file2_parsed = parse("tests/fixtures/file2.json")


def parse(path):
    PARSERS = {
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
        ".json": json.load
    }
    extension = os.path.splitext(path)[1].lower()
    res = PARSERS[extension]((open(path)))
    # print("parse res", res)
    return res
