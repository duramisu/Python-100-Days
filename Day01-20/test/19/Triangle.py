
class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        '''判断三条边能否构成三角形的静态函数'''
        return a + b > c and \
            b + c > a and \
            c + a > b

    @property
    def perimeter(self):
        '''计算三角形周长的属性方法,将方法作为属性使用'''
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(3, 4, 5)
print(f'周长: {t.perimeter}')
print(f'面积: {t.area}')
