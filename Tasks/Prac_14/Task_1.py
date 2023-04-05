import time


def testTime(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")
    return wrapper


def list_append(n):
    l1 = list()
    for i in range(n):
        if i % 2 == 0:
            l1.append(i)
    if n % 2 == 0:
        l1.append(n)
    return l1


def list_comprehensions(n):
    l1 = [i for i in range(n) if i % 2 == 0]
    if n % 2 == 0:
        l1.append(n)
    return l1


test1 = testTime(list_append)
test1(1000000)
test2 = testTime(list_comprehensions)
test2(1000000)
