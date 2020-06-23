def num_divisors(n):
    i = 1
    counter = 0
    while i * i <= n:
        if n % i == 0:
            counter += 1 if i * i == n else 2
        i += 1
    return counter


def main():
    triangle_number = 0
    largest = 0

    for i in range(1, int(1e100)):
        triangle_number += i
        num_divs = num_divisors(triangle_number)
        if num_divs > largest:
            largest = num_divs
            print(f'New largest: {triangle_number} -> {largest}')
        if largest > 500:
            print(f'Answer: {triangle_number}')
            break


if __name__ == '__main__':
    main()
