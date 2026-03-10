# 核心理念：如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子。
# 鸭子类型是一种编程风格，它不检查对象的类型，只关注对象能否“做某件事”（是否有对应的方法）。

# 鸭子多态
class Dog:
    def speak(self):
        print('汪汪汪！')


class Cat:
    def speak(self):
        print('喵喵喵！')


class computer:
    def speak(self):
        print('滋滋滋！')


class Person:
    def speak(self):
        print('人类正在说话！')


def make_sound(animal):
    animal.speak()


make_sound(Dog())
make_sound(Cat())
make_sound(computer())
make_sound(Person())
