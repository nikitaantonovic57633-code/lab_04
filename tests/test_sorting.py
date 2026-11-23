import random
import pytest

from algo_lab.sorting import bubble_sort

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([7]) == [7]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([3, -2, 3, 1, 0]) == [-2, 0, 1, 3, 3]


def test_initial_list_bubble_sort():
    lst = [5, 4, 1, 2, 10]
    copy = lst.copy()
    assert bubble_sort(lst) is not lst
    assert lst == copy


def test_invalid_type_bubble_sort():
    with pytest.raises(TypeError):
        bubble_sort((3, 1))
    with pytest.raises(TypeError):
        bubble_sort([3, "1"])
    with pytest.raises(TypeError):
        bubble_sort([True, 1])


def test_random_list_bubble_sort():
    rng = random.Random(52)
    lst = [rng.randint(-100, 100) for _ in range(rng.randint(1, 25))]
    assert bubble_sort(lst) == sorted(lst)
    lst = [rng.randint(-100, 100) for _ in range(rng.randint(1, 25))]
    assert bubble_sort(lst) == sorted(lst)
    lst = [rng.randint(-100, 100) for _ in range(rng.randint(1, 25))]
    assert bubble_sort(lst) == sorted(lst)