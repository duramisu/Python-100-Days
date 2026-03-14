# 1.函数也是对象
# a = 1
# b1 = [1, 2, 3]
# c1 = 'hello world'
# print(type(a))
# print(type(b1))
# print(type(c1))


# def func():
#     print('hello world')


# f1 = func
# f1()
# print(id(func))
# print(id(f1))

# 2.函数可以动态添加属性
# def func():
#     print('hello world')


# func.a = 1
# func.b = 2

# print(func.a)
# print(func.b)

# 3.函数可以赋值给变量
# def func():
#     print('hello world')

# a = func
# a()


# 4.可变参数 vs 不可变参数
# 不可变参数
# a = 666


# def speak(data):
#     print(data)
#     data = 888
#     print(data)


# speak(a)
# print(a)

# 可变参数
# a = [1, 2, 3]


# def speak(data):
#     print(data)
#     data.append(4)
#     print(data)


# speak(a)
# print(a)

# 5.函数也可以作为参数
# def speak(data):
#     print(data)


# def func(f, msg):
#     f(msg)
#     print('func is called')


# func(speak, 'hello world')

# 6.函数也可以作为返回值

def func():
    def speak(msg):
        print(msg)
    return speak


func()('hello')
