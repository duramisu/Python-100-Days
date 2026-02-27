# 1.使用 index 方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标。
# fruits = ['香蕉', '苹果', '橙子', '香蕉']
# result = fruits.index('橙子')
# print(result)

# 2.使用 count 方法，统计某个元素在列表中出现的次数，返回值是：元素出现的次数。
# fruits = ['香蕉', '苹果', '橙子', '香蕉']
# result = fruits.count('苹果')
# print(result)

# 3.使用 reverse 方法，对列表进行反转（会改变原列表）。
# fruits = ['香蕉', '苹果', '橙子', '香蕉']
# fruits.reverse()
# print(fruits)

# 4.使用 sort 方法，对列表排序（默认从小到大），若想从大到小，可以将 reverse 参数设为True。
# 4.1 若列表中的元素：都是数字，则按照数字的大小顺序进行排序。
# nums = [23, 11, 32, 30, 17]
# nums.sort(reverse=False)
# print(nums)


# 4.2 若列表中的元素：既有数字，又有字符串，那就会报错。
# nums = [23, 11, 32, 30, 17, "苹果"]
# nums.sort()
# print(nums)

# 4.3 若列表中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序
fruits = ['香蕉', '苹果', '橙子', '香蕉']
# 中文转换Unicode
print([ord(char) for char in '香蕉'])

fruits.sort()
print(fruits)

# 备注：所有的列表方法，都只作用于“当前层”的元素（浅层操作），不会自动进入嵌套的“里层”结构中。
