import math


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def proper_divisors(n):
    result = {1}
    i = 2
    while i * i <= n:
        if n % i == 0:
            result.add(i)
            result.add(n // i)
        i += 1
    return sorted(result)


def _unit_tests():
    message = '{}, Input: {}, Expected: {}, Got: {}'
    is_prime_test = [(-1, False), (0, False), (1, False), (2, True), (3, True),
                     (4, False), (5, True), (6, False), (7, True), (8, False),
                     (9, False), (10, False), (11, True), (12, False)]
    proper_divisors_test = [(1, [1]), (2, [1]), (3, [1]), (4, [1, 2]),
                            (5, [1]), (6, [1, 2, 3]), (7, [1]), (8, [1, 2, 4]),
                            (9, [1, 3]), (10, [1, 2, 5]), (11, [1]),
                            (12, [1, 2, 3, 4, 6])]
    function_tests = [(is_prime, is_prime_test),
                      (proper_divisors, proper_divisors_test)]
    for func, test in function_tests:
        for inp, out in test:
            res = func(inp)
            assert res == out, message.format(func.__name__, inp, out, res)


if __name__ == '__main__':
    _unit_tests()
    print('Unit tests passed!')
