# 21124


def main():
    table = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        1000: 'onethousand'
    }

    for i in range(1, 100):
        if i not in table:
            table[i] = table[i - i % 10] + table[i % 10]

    for i in range(1, 10):
        table[i * 100] = table[i] + 'hundred'

    for i in range(1, 1001):
        if i not in table:
            table[i] = table[i - i % 100] + 'and' + table[i % 100]

    print(table)
    print(len(''.join(table.values())))


if __name__ == '__main__':
    main()
