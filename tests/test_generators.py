from algo_lab.generators import sorted_list, reversed_list, random_list, nearly_sorted_list, duplicate_list

def test_generator():
    assert sorted_list(5) == [0, 1, 2, 3, 4]
    assert reversed_list(5) == [4, 3, 2, 1, 0]
    assert nearly_sorted_list(2, seed=52) == [1, 0]


def test_empty_generator():
    assert sorted_list(0) == []
    assert reversed_list(0) == []
    assert nearly_sorted_list(0) == []
    assert duplicate_list(0) == []
    assert random_list(0) == []


def test_same_seed_generator():
    assert random_list(20, seed=52) == random_list(20, seed=52)
    assert nearly_sorted_list(20, seed=52) == nearly_sorted_list(20, seed=52)
    assert duplicate_list(20, seed=52) == duplicate_list(20, seed=52)


def test_different_seed_generator():
    a = random_list(20, seed=53)
    b = random_list(20, seed=52)
    assert len(a) == len(b) == 20
    assert a != b


def test_duplicate_list():
    lst = duplicate_list(20, seed=52)
    assert len(lst) == 20
    assert len(set(lst)) <= 5