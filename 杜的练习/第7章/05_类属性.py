# 定义一个Person类
class Person:
    # 类属性
    max_age = 120
    plant = '地球'
    # 初始化方法
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        if age > Person.max_age:
            self.age = Person.max_age
        else:
            self.age = age

# 访问类属性
# print(Person.max_age)
# print(Person.plant)

p1 = Person('张三', 128, '男')
p2 = Person('李四', 22, '女')

# print(p1.name, p1.age, p1.gender)
# print(p2.name, p2.age, p2.gender)

# print(p1.max_age)
# print(p2.max_age)

# p1.max_age = 130
# print(p1.max_age)
# print(Person.max_age)


print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
