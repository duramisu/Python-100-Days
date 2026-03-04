# 练习一：水果清单
fruits = {
    '苹果': 4.5,
    '香蕉': 3.2,
    '橙子': 5.8,
    '草莓': 12.0,
    '哈密瓜': 8.8
}

# 需求1：打印所有的水果
for fruit in fruits:
    print(fruit)

# 需求2：找到最贵水果
for fruit in fruits:
    if fruits[fruit] == max(fruits.values()):
        print(fruit)


# --------------------------------------------------------------------

# 练习二：学生成绩表
students = [
    {
        'name': '张三',
        'scores': {'语文': 88, '数学': 92, '英语': 95}
    },
    {
        'name': '李四',
        'scores': {'语文': 75, '数学': 83, '英语': 80}
    },
    {
        'name': '王五',
        'scores': {'语文': 92, '数学': 95, '英语': 88}
    }
]

# 需求1：计算每位学生的平均分
for student in students:
    avg_scode = sum(student['scores'].values())/len(student['scores'])
    print(f'{student["name"]}的平均分是：{avg_scode:.1f}')


# 需求2：找到总分最高的学生
max_score = 0
max_student = ''
for student in students:
    total_score = sum(student['scores'].values())
    if total_score > max_score:
        max_score = total_score
        max_student = student['name']
print(f'{max_student}的总分最高，总分是：{max_score}')


# --------------------------------------------------------------------

# 练习三：评论内容
comment = '这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1：统计“好喝”出现次数
count = comment.count('好喝')
print(f'“好喝”出现次数是：{count}')

# 需求2：将字符串中的“贵”替换为“略高”
new_comment = comment.replace('贵', '略高')
print(new_comment)

# 需求3：是否包含“推荐”两个字
print('推荐' in comment)
