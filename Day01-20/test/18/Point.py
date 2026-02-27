class Point:
    """平面上的点"""

    def __init__(self, x=0, y=0):
        """初始化方法
        :param x: x坐标
        :param y: y坐标
        """
        self.x = x
        self.y = y

    def distince_to(self, other):
        """计算两点之间的距离
        :param other: 另一个点
        :return: 两点之间的距离
        """
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


if __name__ == '__main__':
    p1 = Point(3, 5)
    p2 = Point(6, 9)
    print(p1)
    print(p2)
    print(p1.distince_to(p2))
