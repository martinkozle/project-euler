# 1074

cache = {}


def rec(row, col, triangle):
    if (row, col) in cache:
        return cache[row, col]
    if row == len(triangle):
        return 0
    best = max(rec(row + 1, col, triangle), rec(row + 1, col + 1, triangle))
    cache[row, col] = best + triangle[row][col]
    return cache[row, col]


def main(file_name):
    with open(f'data/{file_name}', 'r') as f:
        triangle = [list(map(int, line.split())) for line in f]

    print(triangle)
    print(rec(0, 0, triangle))
    print(cache)


if __name__ == '__main__':
    main('018.txt')
