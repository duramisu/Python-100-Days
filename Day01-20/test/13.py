
from os import name


def testDic():
    dic = {'a': 1, 'b': 2, 'c': 3}
    print(dic['a'])
    print(dic.get('b'))
    print(dic.get('c', 4))        
    print(dic.get('d', 5))
    print(dic)

def testDic1():
    dic = {'a': 1, 'b': 2, 'c': 3}
    print(dic)


def testDic2():
    p1 = {
        'name': '张三',
        'age': 18 ,
        'sex': '男'
    }
    p2 = {
        'name': '李四',
        'age': 19,
        'sex': '女'
    }
    print(p1)
    print(p2)

def testDic3():
    p1 = dict(name='张三', age=18, sex='男')
    print(p1)
    print(p1.get('name'))
    print(p1['name'])
    for key in p1:
        print(f'{key}={p1[key]}')

def testDic4():
    p1 = dict(name='张三', age=18, sex='男')
    p2 = dict(teacher='王五', age=20, sex='女', nature='温柔')
    p1.update(p2)
    print(p1)

def testDic5():
    p1 = dict(name='张三', age=18, sex='男',address='北京')
    p1.pop('address')
    print(p1)
    p1.popitem()
    print(p1)
    p1.clear()
    print(p1)

def countChar():
    '''输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。'''
    text = input('请输入一段话：')
    dic = {}
    for char in text:
        if char.isalpha():
            dic[char] = dic.get(char, 0) + 1
    for key, value in sorted(dic.items(), key=lambda item: item[1], reverse=True):
        print(f'{key}={value}')

def testDic6():
    '''**例子2**：在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。'''
    stocks = {
        'APPLE': 150,
        'GOOGLE': 250,
        'Microsoft': 200,
        'Amazon': 300,
        'Facebook': 100
    }
    stocks2 = {key : value for key, value in stocks.items() if value > 100}
    print(stocks2)




def main():
    testDic6()
    

if __name__ == '__main__':
    main()
