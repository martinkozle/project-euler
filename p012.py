# 76576500
from eulerlib import proper_divisors


def main():
    triangle_number = 0
    largest = 0

    for i in range(1, int(1e100)):
        triangle_number += i
        num_divs = len(proper_divisors(triangle_number))
        if num_divs > largest:
            largest = num_divs
            print(f'New largest: {triangle_number} -> {largest}')
        if largest > 500:
            print(f'Answer: {triangle_number}')
            break


if __name__ == '__main__':
    main()
