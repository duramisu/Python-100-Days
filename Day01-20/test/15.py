'''随机验证码'''
import random
import string

ALL_CHAR = string.ascii_letters+string.digits


def generate_code(code_len=4):
    '''生成随机验证码'''
    code = ''
    for _ in range(code_len):
        index = random.randint(0, len(ALL_CHAR) - 1)
        code += ALL_CHAR[index]
    return code


def main():
    for _ in range(10):
        print(generate_code(6))


if __name__ == '__main__':
    main()
