import pytest

from algo_lab.fibonacci import fib_iterative, fib_recursive

def test_fibonacci():
    assert fib_iterative(0) == 0
    assert fib_recursive(0) == 0
    assert fib_iterative(1) == 1
    assert fib_recursive(1) == 1
    assert fib_iterative(2) == 1
    assert fib_recursive(2) == 1
    assert fib_iterative(6) == 8
    assert fib_recursive(6) == 8


def test_negative_fibonacci():
    with pytest.raises(ValueError):
        fib_iterative(-1)
    with pytest.raises(ValueError):
        fib_recursive(-1)


def test_invalid_type_fibonacci():
    with pytest.raises(TypeError):
        fib_iterative(5.2)
    with pytest.raises(TypeError):
        fib_iterative(True)
    with pytest.raises(TypeError):
        fib_recursive(5.2)
    with pytest.raises(TypeError):
        fib_recursive(True)