import pytest
from calculator import add, subtract, multiply, divide, calculate


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


def test_calculate_expression():
    assert calculate("3 + 4") == 7.0
    assert calculate("10 - 3") == 7.0
    assert calculate("6 * 7") == 42.0
    assert calculate("15 / 3") == 5.0


def test_calculate_invalid():
    with pytest.raises(ValueError):
        calculate("no operator here")
