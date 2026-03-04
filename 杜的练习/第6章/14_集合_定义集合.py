# 定义有内容的【可变集合】
# s1 = {10, 20, 30, 40, 50}
# s2 = {'shanxi', 'beijing', 'shanghai'}
# s3 = {10, 'hello', True, 1, 12.4}
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 定义有内容的【不可变集合】
# s1 = frozenset({10, 20, 30, 40, 50})
# s2 = frozenset({'shanxi', 'beijing', 'shanghai'})
# s3 = frozenset({10, 'hello', True, 1, 12.4})
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# frozenset 接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】
# s1 = frozenset([10, 20, 30, 40, 50])
# s2 = frozenset((10, 20, 30, 40, 50))
# s3 = frozenset('hello')
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)


# 定义空集合（可变集合）
# s1 = set()
# print(type(s1), s1)


# 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
# s1 = {}
# print(type(s1), s1)


# 定义空集合（不可变集合）
# s1 = frozenset()
# print(type(s1), s1)

# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# 通俗理解：只有“不可变”的东西，才能安全的放进集合里
s1 = set({10, 20, 30, 40, 50, frozenset({1, 2, 3})})
print(type(s1), s1)

s2 = set({10, 20, 30, 40, 50, set({1, 2, 3})})
print(type(s2), s2)
