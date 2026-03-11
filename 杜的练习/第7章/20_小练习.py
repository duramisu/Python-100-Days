"""
'************学生管理************'
'1. 添加学生'
'2. 删除学生'
'3. 查看所有学生'
'4. 录入成绩'
'5. 退出'
"""
from datetime import datetime


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # 给每个学生添加一个唯一的学号，格式为：年份+三位计数器，例如2023001
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'
        self.score = {}
        Student.count += 1

    # 计算平均成绩
    def calcu_avg(self):
        if not self.score:
            return 0
        return sum(self.score.values()) / len(self.score)

    def add_score(self, subject, score):
        self.score[subject] = score

    def __str__(self):
        return f'姓名:{self.name} 年龄:{self.age} 性别:{self.gender} 成绩:{self.score} 平均分:{self.calcu_avg():.1f}'


class Manager:
    def __init__(self):
        self.students = []

    # 添加学生
    def add_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        gender = input('请输入性别：')
        # 创建学生实例对象
        stu = Student(name, age, gender)
        # 将当前学生添加到stu_list列表中
        self.students.append(stu)
        print(f'添加成功！学号是：{stu.stu_id}')

    # 删除学生
    def del_student(self):
        stu_id = input('请输入您要删除的学生学号：')
        for stu in self.students:
            if stu.stu_id == stu_id:
                self.students.remove(stu)
                print(f'删除成功，删除的学生信息为：{stu}')
                return
        print('输入的学号有误,未找到该学生！')

    # 查看所有学生
    def show_all_students(self):
        if self.students:
            for stu in self.students:
                print(stu)
        else:
            print('暂无学生！')

    # 录入成绩
    def add_score(self):
        stu_id = input('请输入学生学号：')
        for stu in self.students:
            if stu.stu_id == stu_id:
                # 输入成绩字符串，格式为：学科-分数，学科-分数
                score_str = input('请输入成绩(学科-分数,学科-分数)：')
                # 将输入的多个成绩，按照逗号拆分，形成成绩列表
                score_list = score_str.replace('，', ',').split(',')
                # 循环成绩列表，依次添加成绩
                for item in score_list:
                    # 将成绩拆分为学科和分数
                    subject, score = item.split('-')
                    # 添加成绩
                    stu.add_score(subject, float(score))
                print('添加成功！')
            return
        print('输入的学号有误,未找到该学生！')

    def run(self):
        while True:
            print('************学生管理************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')
            choice = input('请输入您的选择：')
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.del_student()
            elif choice == '3':
                self.show_all_students()
            elif choice == '4':
                self.add_score()
            elif choice == '5':
                print('退出系统！')
                break
            else:
                print('输入有误，请重新输入！')


m1 = Manager()
m1.run()
