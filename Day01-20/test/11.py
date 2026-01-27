def testStr():
    str1 = "hello world"
    str2 = 'hello world'
    str3 = '''hello 
            world'''
    s1 = '\'hello, world!\''
    s2 = '\\hello, world!\\'
    s3 = r'\\\\\hello '' aaa world!!! '
    print(s1)
    print(s2)
    print(str1)
    print(str2)
    print(str3)
    print(s3)


def testStr2():
    s = 'I Love You!'
    words = s.split(' ')
    print('~'.join(words))


def testStr3():
    s = 'hello world'
    words = s.split(' ')
    print('~~'.join(words))


def main():
    testStr2()
    testStr3()


if __name__ == '__main__':
    main()
