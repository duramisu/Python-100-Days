
def testList():
    list = [x*x for x in range(1, 10)]
    print(list)


def testList1():
    list = [x*x for x in range(1, 10) if x*x % 2 == 0]
    print(list)


def main():
    testList()
    testList1()


if __name__ == '__main__':
    main()
