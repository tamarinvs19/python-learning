from random import randint
m = 10000
def one():
    xs = []
    for i in range(m):
        if i % 2 == 0 and i**4 < 100:
            xs.append(i)
def two():
    xs = [i for i in range(m) if i % 2 == 0 and i**4 < 100]

def one_r():
    length = randint(0, m)
    xs = []
    for _ in range(length):
        r = randint(0, m)
        xs.append(r)
def two_r():
    length = randint(0, m)
    xs = [randint(0, m) for _ in range(length)]
    
