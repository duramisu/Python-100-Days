import time


def is_armstrong(num):
    i = 0
    while i < 100:
        i += 1
        print(i)
        time.sleep(1)


def find_armstrong_numbers():
    """
    找出100到999范围内的水仙花数
    """
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


def main():
    find_armstrong_numbers()


if __name__ == '__main__':
    main()
