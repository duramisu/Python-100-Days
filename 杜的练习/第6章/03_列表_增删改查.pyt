# 新增操作
# 方式一：通过列表的append方法，在列表尾部追加一个元素
# list1 = [11, 22, 33, 44, 55]
# list1.append(666)
# print(list1)

# 方式二：通过列表的insert方法，在列表的指定下标处添加一个元素
# list1 = [11, 22, 33, 44, 55]
# list1.insert(2, 66)
# print(list1)

# 方式三：通过列表的extend方法，将可迭代对象中的内容依次取出，追加到列表尾部
# list1 = [11, 22, 33, 44, 55]
# list1.extend([66, 77, 88])
# print(list1)

# 删除操作
# 方式一：通过列表的pop方法，删除指定位置的元素，并返回该元素
# list1 = [11, 22, 33, 44, 55]
# result = list1.pop(2)
# print(result)
# print(list1)

# 方式二：通过列表的remove方法，删除列表中第一次出现的指定值
# list1 = [11, 22, 33, 44, 55, 11, 22]
# list1.remove(11)
# print(list1)

# 方式三：通过列表的clear方法，删除列表中所有的元素（清空列表）
# list1 = [11, 22, 33, 44, 55]
# list1.clear()
# print(list1)


# 方式四：通过del关键字，删除指定元素
# list1 = [11, 22, 33, 44, 55]
# del list1[2]
# print(list1)

# 修改操作
list1 = [11, 22, 33, 44, 55]
list1[0] = 111
print(list1)

# 查询操作
print(list1[0])
print(list1[1])
