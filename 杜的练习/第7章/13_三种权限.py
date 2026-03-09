
class Person:
    def __init__(self, name, age, idcard):
        self.name = name        # 公有属性：当前类中、子类中、类外部，都可以访问
        self._age = age         # 受保护的属性：当前类中、子类中，都可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类中访问

    def speak(self):
        print(f'我叫{self.name}，年龄是{self._age}，身份证是{self.__idcard}')


class Student(Person):
    def __init__(self, name, age, idcard, grade):
        super().__init__(name, age, idcard)
        self.__grade = grade

    def study(self):
        print(f'{self.name}正在学习{self.__grade}年级')


p1 = Person('张三', 18, '110333222323131')
p1.speak()

print(p1._age)
# __idcard为私有属性，不可在类外部访问
# print(p1.__idcard)
