from typing import Optional, List, Iterable


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_generator(*, limit: Optional[int] = None,
                    count: Optional[int] = None) -> Iterable[int]:
    i = 2
    primes = []
    while ((limit is None or i < limit) and
           (count is None or len(primes) < count)):
        flag = True
        for prime in primes:
            if prime * prime > i:
                break
            if i % prime == 0:
                flag = False
                break
        if flag:
            primes.append(i)
            yield i
        i += 1


def proper_divisors(n: int) -> List[int]:
    result_first = [1]
    result_last = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            result_first.append(i)
            if i != n // i:
                result_last.append(n // i)
        i += 1
    result = result_first + result_last[::-1]
    return result
