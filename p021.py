def main():
    table = {}
    result = 0
    for i in range(1, 10000):
        divs_sum = sum(j for j in range(1, i) if i % j == 0)
        if divs_sum in table and table[divs_sum] == i:
            print(i, divs_sum)
            result += divs_sum + i
        table[i] = divs_sum
    print(result)


if __name__ == '__main__':
    main()
