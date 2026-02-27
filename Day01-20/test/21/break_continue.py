
def break_continue():
    for i in range(1, 5):
        print(f"第{i}天")
        print("吃饭", i)
        continue
        print("睡觉", i)


def main():
    break_continue()


if __name__ == '__main__':
    main()
