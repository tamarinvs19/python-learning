def is_prime(x):
    '''
    This function test the number x on prime
    Retrun True if x is prime and fasle if not
    x - number
    '''
    if x in {1, 0}:
        return False
    else:
        i = 2
        res = True
        while i <= int(x**0.5): 
            if x % i == 0:
                res = False
                break
            i += 1
        return res

