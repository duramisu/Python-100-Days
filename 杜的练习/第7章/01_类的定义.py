# 定义一个Person类（类名通常使用：大驼峰写法）
class Person:
    # 说明：当一个函数被定义在了类中时，那这个函数就被称为：方法。
    # __init__方法：初始化方法，主要作用：给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在创建的实例对象（self）、其它的自定义参数
    # 当我们以后编写代码去创建Person类实例的时候，Python会自动调用__init__方法
    def __init__(self, name, age, sex):
        print('Person类的实例对象被创建了')
        self.name = name
        self.age = age
        self.sex = sex
        print(f'创建的实例对象的name属性值是：{self.name}')
        print(f'创建的实例对象的age属性值是：{self.age}')
        print(f'创建的实例对象的sex属性值是：{self.sex}')


person1 = Person('张三', 18, '男')
print(person1)
print(person1.name)
print(person1.age)
print(person1.sex)
