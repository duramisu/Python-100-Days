# 表达式：执行后能得到值的代码，就是表达式（表达式最终会形成一个值，可以写在任何需要值的地方）。
# a = 1+1
# b = 2+2
# c = a+b
# print(a)
# print(b)
# print(c)
# d = [1, 2, 3, 4, 5]
# print(d*2)

# 条件表达式：根据条件的真假，在两个值中二选一的表达式（又称：三元表达式、三目运算符）。
# age = 21
# is_adult = '成年' if age >19 else '未成年'
# print(is_adult)

# 传统的if-else去写：
# if age>18:
#     print('成年')
# else :
#     print('未成年')

# 条件表达式去写：值1 if 条件 else 值2
rain = True
eat = '外卖' if rain else '出去吃'
print(eat)

# 条件表达式的使用场景：简单的二选一场景
is_login = False
login_msg = '欢迎回来！' if is_login else '请先登录！'
print(login_msg)
