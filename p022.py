def main():
    with open('data/022.txt', 'r') as f:
        line = f.readline()
        names = list(map(lambda x: x.strip('"'), line.split(',')))
    names.sort()
    print(names)
    total_score = 0
    for i, name in enumerate(names):
        total_score += (sum(map(lambda x: ord(x) - ord('A') + 1, name))
                        * (i + 1))
    print(total_score)


if __name__ == '__main__':
    main()
