"""99乘法表"""


def print_99_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{j} * {i} = {i*j}\t', end='')
        print()


def main():
    print_99_table()


if __name__ == '__main__':
    main()
