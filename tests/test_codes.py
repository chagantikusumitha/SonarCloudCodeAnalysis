# tests/test_your_code.py
from src.codes import add_numbers, multiply_numbers

import pytest
from src.codes import add_numbers, multiply_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(2, 2) == 4
def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(0, 0) == 5
