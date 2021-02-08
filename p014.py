# 837799

cache = {1: 1}


def rec(n):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        res = rec(n // 2) + 1
    else:
        res = rec(3 * n + 1) + 1
    cache[n] = res
    return res


def main():
    print(max((rec(i), i) for i in range(1, 1000000))[1])


if __name__ == '__main__':
    main()
