from random import randint, choice
from collections import Counter

def gen_number():
    a = randint(0, 2)
    b = choice([x for x in range(10) if x != a])
    return a*10+b
def one():
    number = gen_number()
    rs = Counter([gen_number() == number for _ in range(10**4)])
    print(rs)
    print(rs[1] / (rs[1]+rs[0]))

def two():
    rs = len([x for x in range(30) if x%10 != x//10])
    print(1/rs)

one()
two()
