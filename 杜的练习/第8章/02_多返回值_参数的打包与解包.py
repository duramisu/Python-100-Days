# 一、函数的多返回值
# def cmp_num(x, y):
#     res1 = x - y
#     res2 = x + y
#     return res1, res2


# r1, r2 = cmp_num(10, 20)
# print(r1, r2)

# t1 = cmp_num(20, 30)
# print(t1)

# 二、参数的打包与解包

# 1.打包接收参数：
# def spk(*args, **kewword):
#     print(args)
#     print(kewword)


# spk(1, 2, 3, 4, name='张三', age=18)


# 2.解包传递参数
# *变量名  ：将元组拆解成一个一个独立的位置参数
# **变量名 ：将字典拆解一个一个 key=value 形式的关键字参数
# def add(a, b, c, d, e, f):
#     print(a, b, c)
#     print(d, e, f)


# nums1 = (1, 2, 3)
# list1 = [4, 5, 6]
# dict1 = {'d': 4, 'e': 5, 'f': 6}

# add(*nums1, **dict1)


# 3.打包接收参数 和 解包传递参数 一起使用
def show_info(*args, **kwargs):
    print(args)
    print(kwargs)


nums = (10, 20, 30)
person = {'name': '张三', 'age': 18, 'gender': '男'}

show_info(*nums, **person)
