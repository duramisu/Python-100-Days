"""完成一个健身挑战赛程序"""


def calc_total(*nums):
    """计算总运动量"""
    return sum(nums)


def calc_avg(total, days=7):
    """计算平均值"""
    return total / days


def check_success(total, goal=120):
    """判断本次挑战是否成功"""
    if total >= goal:
        return '✅恭喜！挑战成功！'
    else:
        return '❌抱歉！挑战失败！'


def main(title, duration, goal):
    """
    主函数，用于开始一场挑战赛
    :param title: 挑战赛标题
    :param duration: 挑战赛持续天数
    :param goal: 挑战目标运动量
    """
    print(f'【{title}】【{duration}天】✊️挑战赛（请输入每天的数量）')
    nums = []
    for i in range(duration):
        num = int(input(f'请输入第{i+1}天的运动量：'))
        nums.append(num)
    # 计算总运动量
    total = calc_total(*nums)
    # 计算平均值
    avg = calc_avg(total, duration)
    # 输出统计结果（total 为总运动量，avg 为每天平均运动量）
    print(f'总运动量为：{total}')
    print(f'平均运动量为：{avg}')
    # 判断是否成功
    print(check_success(total, goal))


if __name__ == '__main__':
    main('俯卧撑', 3, 20)
