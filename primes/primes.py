import logging as log


def is_prime(n):
    p = 2
    stop = 0
    while p <= n**0.5 and stop == 0:
        if n % p == 0:
            stop = 1
        p += 1
    print(f'res = {stop==0}, n = {n}')
    return stop == 0

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(239) == True
    assert is_prime(22) == False
    assert is_prime(1024) == False
    assert is_prime(25) == False
    assert is_prime(2**32 - 1) == False

def get_primes(limit):
    with open(f'primes_to_{limit}', 'w') as f:
        ps = [n for n in range(2, limit+1) if is_prime(n)]
        print(ps, file=f)
        print(len(ps))

if __name__ == '__main__':
    get_primes(10**6)

