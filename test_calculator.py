import pytest

from calculator import add, multiply, divide

def test_add():
    # Test add two positive integers
    assert add(1, 2) == 3

    # Test adding a zero
    assert add(5, 0) == 5

    # Test adding two negative integers
    assert add(-1, -2) == -3

def test_multiply():
    # Test multiplying two positive integers
    assert multiply(2, 3) == 6

    # Test multiplying by zero
    assert multiply(5, 0) == 0

    # Test multiplying a positive and a negative integer
    assert multiply(4, -2) == -8

    # Test multiplying two negative integers
    assert multiply(-2, -3) == 6

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)