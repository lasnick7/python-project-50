import pytest
from gendiff.scripts.gendiff import generate_diff

@pytest.fixture
def files_non_nested():
    return {
        "file1_json": "tests/fixtures/non_nested/file1.json",
        "file2_json": "tests/fixtures/non_nested/file2.json",
        "file1_yaml": "tests/fixtures/non_nested/file1.yaml",
        "file2_yaml": "tests/fixtures/non_nested/file2.yaml",
        "file1_yml": "tests/fixtures/non_nested/file1.yml",
        "file2_yml": "tests/fixtures/non_nested/file2.yml",
    }

@pytest.fixture
def files_nested():
    return {
        "file1_json": "tests/fixtures/nested/file1.json",
        "file2_json": "tests/fixtures/nested/file2.json",
        "file1_yaml": "tests/fixtures/nested/file1.yaml",
        "file2_yaml": "tests/fixtures/nested/file2.yaml",
        "file1_yml": "tests/fixtures/nested/file1.yml",
        "file2_yml": "tests/fixtures/nested/file2.yml",
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

@pytest.fixture
def nested():
    res = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    return res



def test_format_stylish_non_nested(files_non_nested, non_nested):
    f = files_non_nested
    assert generate_diff(f["file1_json"], f["file2_json"]) == non_nested
    assert generate_diff(f["file1_yaml"], f["file2_yaml"]) == non_nested
    assert generate_diff(f["file1_yml"], f["file2_yml"]) == non_nested

def test_format_stylish_nested(files_nested, nested):
    f = files_nested
    assert generate_diff(f["file1_json"], f["file2_json"]) == nested
    assert generate_diff(f["file1_yaml"], f["file2_yaml"]) == nested
    assert generate_diff(f["file1_yml"], f["file2_yml"]) == nested