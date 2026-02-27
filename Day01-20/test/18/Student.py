class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习：{course_name}')

    def play(self):
        print(f'{self.name}正在玩耍')


stu1 = Student('王五', 18)
stu2 = Student('张三', 28)

stu1.study('Python程序设计')
stu2.play()
