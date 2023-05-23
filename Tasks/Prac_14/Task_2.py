import functools
import time

def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper


@cache
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


start = time.perf_counter()
fib(20)
print('Время выполнения:', time.perf_counter() - start)
