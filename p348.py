# 1004195061
from tqdm import tqdm


def main():
    d = {}
    j2 = [p*p for p in range(1, 30000)]

    for i in tqdm(range(1, 2000)):
        i3 = i * i * i
        for j in j2:
            s = i3 + j
            if str(s) != str(s)[::-1]:
                continue
            if s not in d:
                d[s] = 0
            d[s] += 1
            if d[s] > 4:
                del d[s]

    print(sum(k for k, v in d.items() if v == 4))


if __name__ == '__main__':
    main()
