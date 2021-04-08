import functools

def n_times(k):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(k):
                func(*args, **kwargs)
        return wrapper
    return inner

@n_times(3)
def do_something():
    print(123)

@n_times(3)
def do_something2(x, y):
    print(x + y)

do_something()
do_something2(239, 1)

