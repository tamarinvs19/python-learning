from functools import wraps
def only_int(func):
    @wraps(func)
    def inner(x):
        '''
        здесь можно устраивать логгирование вызовов
        Это новый инструмент для программирования
        '''
        if isinstance(x , int):
            return func(x)
        else:
            raise ValueError
    return inner

from is_prime import is_prime
is_prime = only_int(is_prime)
# print(help(is_prime))

