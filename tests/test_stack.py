import pytest

from algo_lab.stack import Stack

def test_stack():
    stack = Stack()
    assert len(stack) == 0
    assert bool(stack) == False
    stack.push(0)
    assert len(stack) == 1
    assert bool(stack) == True
    stack.push(20)
    assert len(stack) == 2
    assert bool(stack) == True
    assert stack.peek() == 20
    assert len(stack) == 2
    assert bool(stack) == True
    assert stack.pop() == 20
    assert len(stack) == 1
    assert bool(stack) == True
    assert stack.pop() == 0
    assert len(stack) == 0
    assert bool(stack) == False


def test_stack_empty():
    stack = Stack()
    assert len(stack) == 0
    assert bool(stack) == False
    with pytest.raises(IndexError):
        stack.peek()
    with pytest.raises(IndexError):
        stack.pop()