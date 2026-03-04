# 字典不能使用while循环遍历，但可以使用for循环遍历
d1 = {'张三': 72, '李四': 60, '王五': 85}

for key in d1.keys():
    print(f'{key}的成绩是{d1[key]}')

for value in d1.values():
    print(value)

for item in d1.items():
    print(item)
