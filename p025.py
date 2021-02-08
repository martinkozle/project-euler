# 4782


def main():
    a = b = 1
    counter = 0
    while b < 10 ** 999:
        a, b = b, a + b
        counter += 1
    print(counter + 2)


if __name__ == '__main__':
    main()
