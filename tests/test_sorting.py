import random
import pytest

from algo_lab.sorting import bubble_sort, merge_sort

@pytest.mark.parametrize("func", [bubble_sort, merge_sort])
def test_func(func):
    assert func([]) == []
    assert func([7]) == [7]
    assert func([1, 2, 3]) == [1, 2, 3]
    assert func([3, 2, 1]) == [1, 2, 3]
    assert func([3, -2, 3, 1, 0]) == [-2, 0, 1, 3, 3]


@pytest.mark.parametrize("func", [bubble_sort, merge_sort])
def test_initial_list_func(func):
    lst = [5, 4, 1, 2, 10]
    copy = lst.copy()
    assert func(lst) is not lst
    assert lst == copy


@pytest.mark.parametrize("func", [bubble_sort, merge_sort])
def test_invalid_type_func(func):
    with pytest.raises(TypeError):
        func((3, 1))
    with pytest.raises(TypeError):
        func([3, "1"])
    with pytest.raises(TypeError):
        func([True, 1])


@pytest.mark.parametrize("func", [bubble_sort, merge_sort])
def test_random_list_func(func):
    rng = random.Random(52)
    lst = [rng.randint(-100, 100) for _ in range(rng.randint(1, 25))]
    assert func(lst) == sorted(lst)
    lst = [rng.randint(-100, 100) for _ in range(rng.randint(1, 25))]
    assert func(lst) == sorted(lst)
    lst = [rng.randint(-100, 100) for _ in range(rng.randint(1, 25))]
    assert func(lst) == sorted(lst)