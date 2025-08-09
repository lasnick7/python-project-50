import pytest
from gendiff.scripts.gendiff import generate_diff

@pytest.fixture
def file1_json():
    return "tests/fixtures/file1.json"
