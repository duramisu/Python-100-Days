import random
import time
from functools import lru_cache, wraps


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret_value = func(*args, **kwargs)
        print(f'{func.__name__} 函数执行时间: {time.time() - start}')
        return ret_value
    return wrapper


@record_time
def download(filename):
    print(f'开始下载 {filename}')
    time.sleep(random.randint(2, 5))
    print(f'下载完成 {filename}')


@record_time
def upload(filename):
    print(f'开始上传 {filename}')
    time.sleep(random.randint(2, 5))
    print(f'上传完成 {filename}')


def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


def main():

    # filename = 'Python从入门到实战.pdf'
    # download(filename)
    # upload(filename)

    # download.__wrapped__(filename)
    # upload.__wrapped__(filename)
    # print(fac(5))
    for i in range(1, 51):
        print(fib1(i))


if __name__ == '__main__':
    main()
