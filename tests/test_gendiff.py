import pytest
from gendiff.scripts.gendiff import generate_diff

@pytest.fixture
def files():
    return {
        "file1_json": "tests/fixtures/file1.json",
        "file2_json": "tests/fixtures/file2.json"
    }

@pytest.fixture
def non_nested():
    res = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    return res


def test_format1(files, non_nested):
    f = files
    assert generate_diff(f["file1_json"], f["file2_json"]) == non_nested