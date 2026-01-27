
import random


def list_test():
    item1 = [2, 3, 4, 5, 6]
    item2 = ['a', 'b', 'c', 'd', 'e']
    item3 = [2, True, 'b']

    print(item1)
    print(item2)
    print(item3)

    item4 = list(range(1, 5))
    item5 = list('world')
    print(item4)
    print(item5)


def list_dice_test():
    """
    将一颗色子掷6000次，统计每种点数出现的次数
    """
    count = [0] * 6
    for i in range(6000):
        count[random.randint(0, 5)] += 1

    for i in range(6):
        print(f'{i+1}点出现了{count[i]}次')


def main():
    list_dice_test()


if __name__ == '__main__':
    main()
