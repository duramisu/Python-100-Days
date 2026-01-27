
def random_select():
    """
    双色球随机选号程序
    """
    red_balls = [i for i in range(1, 34)]
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(random.randint(1, 16))
    print(selected_balls)


def main():
    random_select()


if __name__ == '__main__':
    main()
