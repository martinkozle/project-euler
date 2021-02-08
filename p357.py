# 1739023853137
# this one took an hour and 50 minutes to compute
from eulerlib import proper_divisors, prime_generator


from tqdm import tqdm


def main():
    total = 100000000
    primes_set = set(tqdm(prime_generator(limit=total), total=total))
    s = 0
    for i in tqdm(primes_set):
        flag = True
        for d in proper_divisors(i - 1):
            if d + (i - 1) // d not in primes_set:
                flag = False
                break
        if flag:
            s += i - 1
    print(s)


if __name__ == '__main__':
    main()
