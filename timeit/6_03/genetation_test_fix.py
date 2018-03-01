from random import randint, seed
m = 1000

def generate_lists(count):
    res = []
    length = randint(0, m)
    for i in range(0, m):
        if i < count:
            s = 2
        else:
            s = 1
        xs = [randint(s, m) for _ in range(length)]
        res.append(xs)
    return res