"""
循环结构
"""

"""
从1到100的偶数求和
"""
def sum_even_numbers():
    total = 0
    for i in range(2, 101, 2):
        total += i
    print(total)

"""
从1到100的整数求和
"""
def sum_numbers_for():
    total = 0
    for i in range(1, 101):
        total += i
    print(total)

"""
从1到100的整数求和
"""
def sum_numbers_while():
    total = 0
    i = 1
    while i<=100:
        total += i
        i += 2
    print(total)

"""
主函数
"""
def main():
    sum_even_numbers()

"""
测试运行
"""
if __name__ == "__main__":
    main()
