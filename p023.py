from eulerlib import *


def main():
    abundant_sums = set()
    abundant_numbers = []
    result = 0
    for i in range(1, 28124):
        divs_sum = sum(proper_divisors(i))
        if divs_sum > i:
            abundant_numbers.append(i)
            for number in abundant_numbers:
                if number + i > 28123:
                    break
                abundant_sums.add(i + number)
    print(abundant_numbers)
    print(abundant_sums)
    for i in range(1, 28124):
        if i not in abundant_sums:
            result += i
    print(result)


if __name__ == '__main__':
    main()
