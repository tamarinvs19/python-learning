from functools import lru_cache
def fib1(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib1(x-1) + fib1(x-2)

# using lru_cache
@lru_cache(maxsize=None)
def fib(x):
    if x in {1, 0}:
        return x
    else:
        return fib(x-1) + fib(x-2)

print(fib(20))
print(fib.cache_info())
