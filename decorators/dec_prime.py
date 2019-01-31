from functools import wraps
def only_int(func):
    @wraps(func)
    def inner(x):
        if isinstance(x , int):
            return func(abs(x))
        else:
            raise ValueError
    return inner

from is_prime import is_prime
is_prime = only_int(is_prime)
print('-239:', is_prime(-239))
print('238:', is_prime(-238))
