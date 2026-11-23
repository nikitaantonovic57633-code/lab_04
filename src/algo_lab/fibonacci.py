def fib_iterative(n):
    if type(n) != int:
        raise TypeError
    if n < 0:
        raise ValueError
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n):
    if type(n) != int:
        raise TypeError
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)