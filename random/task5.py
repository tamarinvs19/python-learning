from random import sample
from collections import Counter
from itertools import permutations

def one():
    ab = ["К","У","К","Л","А"]
    rs = Counter([sample(ab, len(ab)) == ab for _ in range(10**4)])
    print(rs)
    print(rs[1] / (rs[1] + rs[0]))

def two():
    ab = ["К","У","К","Л","А"]
    count = len({x for x in permutations(ab, 5)})
    print(1/count)

one()
two()
