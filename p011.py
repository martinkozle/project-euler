# 70600674


def main():
    mat = []
    mat.extend([[0] * 26] * 3)

    with open('data/011.txt', 'r') as f:
        for line in f:
            mat.append([0, 0, 0] + list(map(int, line.split(' '))) + [0, 0, 0])

    mat.extend([[0] * 26] * 3)

    print(mat)

    largest_prod = 0

    for y in range(3, 23):
        for x in range(3, 23):
            add_tuples = [(1, 1), (1, 0), (0, 1), (-1, 1)]
            for yi, xi in add_tuples:
                largest_prod = max(largest_prod,
                                   mat[y][x] *
                                   mat[y + 1 * yi][x + 1 * xi] *
                                   mat[y + 2 * yi][x + 2 * xi] *
                                   mat[y + 3 * yi][x + 3 * xi])

    print(largest_prod)


if __name__ == '__main__':
    main()
