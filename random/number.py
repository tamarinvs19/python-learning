from collections import Counter
from random import choice, randint, sample
from pprint import pprint
from itertools import permutations

def one():
    num = list(range(10))
    x = randint(0, 9)

    ys = Counter([x in sample(num, k=3) for _ in range(10**5)])

    pprint(ys)
    print(ys[True] / (ys[True] + ys[False]))

def two():
    num = list(range(10))
    x = randint(0, 9)

    c = Counter([0 in p for p in permutations(num, 3)])

    pprint(c)
    print(c[True] / (c[True] + c[False]) )
    
one()
two()
