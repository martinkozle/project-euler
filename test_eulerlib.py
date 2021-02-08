from eulerlib import is_prime, prime_generator, proper_divisors


def test_is_prime():
    is_prime_cases = [
        (-1, False), (0, False), (1, False), (2, True), (3, True), (4, False),
        (5, True), (6, False), (7, True), (8, False), (9, False), (10, False),
        (11, True), (12, False)
    ]
    for inp, output in is_prime_cases:
        assert is_prime(inp) == output


def test_prime_generator():
    prime_generator_limit_cases = [
        (60, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]),
        (1, [])
    ]
    prime_generator_count_cases = [
        (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (1, [2]),
        [0, []]
    ]
    for inp, output in prime_generator_limit_cases:
        assert list(prime_generator(limit=inp)) == output
    for inp, output in prime_generator_count_cases:
        assert list(prime_generator(count=inp)) == output


def test_proper_divisors():
    proper_divisors_cases = [
        (1, [1]), (2, [1]), (3, [1]), (4, [1, 2]), (5, [1]), (6, [1, 2, 3]),
        (7, [1]), (8, [1, 2, 4]), (9, [1, 3]), (10, [1, 2, 5]), (11, [1]),
        (12, [1, 2, 3, 4, 6])
    ]
    for inp, output in proper_divisors_cases:
        assert proper_divisors(inp) == output
