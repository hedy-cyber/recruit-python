'''
README

HOW TO RUN
    - pytest

'''

import pytest
from count_sum_max_avg import *

# test all valid files are successfully opened and read
@pytest.mark.parametrize("file_path, expected", [
    ("examples/basic.txt", [1, 2, 10, 20]), ("examples/mixed.txt", [-2, -1, 0, 1, 2]),
    ("examples/negative.txt", [-1, -5, -2, -4, -3]), ("examples/single.txt", [42])
])
def test_read_file_no_error(file_path, expected):
    assert read_file(file_path) == expected

# test all valid files are read and their counts are calculated
@pytest.mark.parametrize("file_path, expected", [
    ("examples/basic.txt", 4), ("examples/mixed.txt", 5),
    ("examples/negative.txt", 5), ("examples/single.txt", 1)
])
def test_calc_count(file_path, expected):
    file_lines_int = read_file(file_path)
    assert calc_count(file_lines_int) == expected

# test all valid files are read and their sums are calculated
@pytest.mark.parametrize("file_path, expected", [
    ("examples/basic.txt", 33), ("examples/mixed.txt", 0),
    ("examples/negative.txt", -15), ("examples/single.txt", 42)
])
def test_calc_sum(file_path, expected):
    file_lines_int = read_file(file_path)
    assert calc_sum(file_lines_int) == expected
