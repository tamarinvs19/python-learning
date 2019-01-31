from is_prime import is_prime
from functools import wraps
def sieve_of_eratosthens(a):
    '''
    Return tre sieve of Eratosthens before 'a'
    a - int
    '''
    is_comp = [False] * (a+1)
    is_comp[0] = True
    is_comp[1] = True
    for i, n in enumerate(is_comp):
        if n:
            pass
        else:
            for j in range(2, a//i + 1):
                is_comp[j*i] = True
    p = [i for i in range(a+1) if not is_comp[i]]
    return p


def sieve_prime(func):
    @wraps(func)
    def inner(x):
        if isinstance(x, int):
            x = abs(x)
            lim = 1000
            sieve = sieve_of_eratosthens(lim)
            if x <= lim:
                return x in sieve
            else:
                return func(x)
        else:
            return ValueError 
    return inner

is_prime = sieve_prime(is_prime)
print(is_prime(239))
print(is_prime(1001))
