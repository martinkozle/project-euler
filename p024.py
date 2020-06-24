import itertools


def main():
    generator = itertools.permutations(range(10))
    for _ in range(999999):
        next(generator)
    print(''.join(map(str, next(generator))))


if __name__ == '__main__':
    main()
