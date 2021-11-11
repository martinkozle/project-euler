# 443839
import tqdm


def main():
    nums = []
    for num in tqdm.tqdm(range(10, 1_000_000)):
        if num == sum(int(digit) ** 5 for digit in str(num)):
            nums.append(num)
    print(f'{nums = }\n{sum(nums) = }')


if __name__ == '__main__':
    main()
