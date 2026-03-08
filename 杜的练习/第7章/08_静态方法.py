# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 定义一个静态方法
    @staticmethod
    def static_method():
        print('这是一个静态方法')

    @staticmethod
    def is_adult(age):
        return age >= 18

    @staticmethod
    def mark_id_card(id_card):
        return '*' * 10 + id_card[-4:]

# 调用静态方法

print(Person.__dict__)
Person.static_method()
print(Person.is_adult(18))
print(Person.mark_id_card('123456789012345678'))
