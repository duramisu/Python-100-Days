# 以下这五个函数：既能定义对应的【空容器】，又能将【其他类型】转换为对应的数据类型

# 1.list 函数：1.定义空列表。2.将【可迭代对象】转换为列表
# res1 = list()
# res2 = list('欢迎来到尚硅谷')
# res3 = list(range(10))
# res4 = list({'张三': 75, '李四': 60, '王五': 85}.items())
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 2.tuple 函数：1.定义空元组。2.将【可迭代对象】转换为元组
# res1 = tuple()
# res2 = tuple('欢迎来到尚硅谷')
# res3 = tuple(range(10))
# res4 = tuple({'张三': 75, '李四': 60, '王五': 85}.items())
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 3.set 函数：1.定义空集合。2.将【可迭代对象】转换为集合
# res1 = set()
# res2 = set('欢迎来到尚硅谷')
# res3 = set(range(10))
# res4 = set({'张三': 75, '李四': 60, '王五': 85}.items())
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 4.str 函数：1.定义空字符串。2.将【任意类型】转换为字符串
# res1 = str()
# res2 = str('欢迎来到尚硅谷')
# res3 = str(range(10))
# res4 = str({'张三': 75, '李四': 60, '王五': 85})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 5.dict 函数：1.定义空字典。2.将【可迭代对象】转换为字典
# 备注：交给dict函数的内容必须是键值对才可以，否则就会报错
# res1 = dict()
# res2 = dict({'张三': 75, '李四': 60, '王五': 85})
# res3 = dict([('张三', 75), ('李四', 60), ('王五', 85)])
# res4 = dict((('张三', 75), ('李四', 60), ('王五', 85)))
# res5 = dict({('张三', 75), ('李四', 60), ('王五', 85)})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)
# print(type(res5), res5)


# 所有的数据容器，都支持【成员运算符】： in / not in  作用：判断某个“元素”是否在于容器中。
hobby = ['抽烟', '喝酒', '烫头']
nums = (10, 20, 30, 40, 50)
message = 'hello,atgiugu'
citys = {'北京', '天津', '上海', '重庆'}
score = {'张三': 75, '李四': 60, '王五': 85}

print('喝酒' in hobby)
print(20 in nums)
print('hel' in message)
print('上海' in citys)
print('李四' in score)

print('喝酒' not in hobby)
print(20 not in nums)
print('hel' not in message)
print('上海' not in citys)
print('李四' not in score)
