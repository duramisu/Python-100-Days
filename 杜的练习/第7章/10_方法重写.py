# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')


class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 在子类中，有两种方法调用父类的初始化方法，来实现对继承属性name,age,gender的初始化操作
        super().__init__(name, age, gender)
        # Person.__init__(self, name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

    def study(self, msg):
        super().speak(msg)
        print(f'{self.name}正在学习{msg}')


s1 = Student('李华', 16, '男', '2025001', '初二')
s1.study('Python程序设计')
