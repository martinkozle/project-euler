# 1389019170
# this took 27 minutes to compute
from math import sqrt

from tqdm import trange


def main():
    template = '1{}2{}3{}4{}5{}6{}7{}8{}9{}0'
    num_sqrt = None
    for i in trange(1000000000):
        num = int(template.format(*f'{i:09}'))
        num_sqrt = int(sqrt(num))
        if num_sqrt * num_sqrt == num:
            break
    print(num_sqrt)


if __name__ == '__main__':
    main()
