from random import randint, seed
m = 10000

def one_rf():
    
    length = randint(0, m)
    #print(1, length)
    xs = []
    for _ in range(length):
        r = randint(0, m)
        xs.append(r)
def two_rf():
    
    length = randint(0, m)
    #print(2, length)
    xs = [randint(0, m) for _ in range(length)]
