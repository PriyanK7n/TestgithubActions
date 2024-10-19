# from src.mathOperations import add, sub, multiply, divide
from src.mathOperations import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add(5, 9) == 14
    assert add(-11, 11) == 0
    assert add(0, 10000) == 10000


def test_sub():
    assert subtract(5, 2) == 3
    assert subtract(11, 11) == 0
    assert subtract(-11, 11) == -22
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 6) == 24
    assert multiply(0, 6) == 0
    assert multiply(0, -11) == 0
    assert multiply(-11, -11) == 121


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 1) == 10
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
