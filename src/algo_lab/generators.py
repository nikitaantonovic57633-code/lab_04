import random

def random_list(size, seed=None):
    rng = random.Random(seed)
    result = []
    for i in range(size):
        result.append(rng.randint(-size, size))
    return result


def sorted_list(size):
    return [i for i in range(size)]


def reversed_list(size):
    return [i for i in range(size - 1, -1, -1)]


def nearly_sorted_list(size, seed=None):
    lst = sorted_list(size)
    if len(lst) < 2:
        return lst
    i = random.Random(seed).randrange(size - 1)
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def duplicate_list(size, seed=None):
    rng = random.Random(seed)
    result = []
    for i in range(size):
        result.append(rng.randint(0, 4))
    return result