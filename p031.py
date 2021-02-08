# 73682


def main():
    b = [1, 2, 5, 10, 20, 50, 100, 200]
    a = [[1] * 201 for _ in range(8)]
    for y in range(1, 8):
        for x in range(201):
            a[y][x] = a[y-1][x] + (a[y][x-b[y]] if x-b[y] >= 0 else 0)
    print(a[7][200])


if __name__ == '__main__':
    main()
