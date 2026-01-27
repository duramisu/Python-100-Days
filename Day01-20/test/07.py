
def baiqianbaiji():
    """
    百钱百鸡问题
    """
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5*x + 3*y + z/3 == 100:
                print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')


def main():
    baiqianbaiji()


if __name__ == '__main__':
    main()
