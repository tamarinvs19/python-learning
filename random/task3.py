from random import choice, randint, sample
from pprint import pprint
from itertools import product
from collections import Counter

def check(xs):
    return len(set(xs)) == 4

def one():
    rs = Counter([len({randint(0, 4) for _ in range(6)}) == 4 for _ in range(10**4)])

    print(rs)
    print(rs[True] / (rs[0]+rs[1]))

def two():
    rs = Counter([xs.count(0) == 1 for xs in product(range(7), repeat=5)  if sum(xs) == 6])
    pprint(rs)
    print(rs[1] / (rs[1] + rs[0]))

one()
two()

