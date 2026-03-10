# 多态的概念：同一个方法名，在不同的对象上调用时，能呈现出不同的行为。
# Python中支持：标准多态、鸭子多态
class Animal:
    def speak(self):
        print('动物正在发出声音Animal！')


class Dog(Animal):
    def speak(self):
        print('汪汪汪！')


class Cat(Animal):
    def speak(self):
        print('喵喵喵！')


class Pig(Animal):
    def speak(self):
        print('哼哼哼！')


def make_sound(animal: Animal):
    animal.speak()


d1 = Dog()  # 创建一个Dog类的实例对象
c1 = Cat()  # 创建一个Cat类的实例对象
p1 = Pig()  # 创建一个Pig类的实例对象
make_sound(d1)
make_sound(c1)
make_sound(p1)
