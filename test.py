import pytest
from calculator import add, subtract, multiply, divide, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    # Uncomment below once you enable the zero-division check in calculator.py
    # with pytest.raises(ValueError):
    #     divide(5, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1