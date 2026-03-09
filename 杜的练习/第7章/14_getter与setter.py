class Person:
    max_age = 120

    def __init__(self, name, age, idcard):
        self.name = name        # 公有属性：当前类中、子类中、类外部，都可以访问
        self._age = age         # 受保护的属性：当前类中、子类中，都可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类中访问
