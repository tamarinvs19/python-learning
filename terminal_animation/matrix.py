from random import randint
from time import sleep


y = 1
def g(x):
    global y
    y = (y + 10) % 239
    return (y%139)**2 + 2*(x%120)**2 +5

t = 1
def h(x):
    global y, t
    y = (y + 10) % t
    t = (t + 10) % 101+1
    return (y%139)**3 + 2*(x%120)**2 +5

def i(x):
    global y, t
    y = (y + 10) % t
    t = (t + 10) % 101+1
    return (y%139)**2 - 2*(x%120)**2 +5

def f(x):
    global y, t
    y = (y + 10) % t
    t = (t + 10) % 101+1
    return (y%230)**2 - 2*(x%20)**2 * t + h(23 + x) 

def main():
    # for i in range(100):
    while True:
        ls = [f(x) % 7 for x in range(100)]
        print(''.join(map(lambda x: ' ' if x != 0 else str(1), ls)))
        sleep(0.1)


if __name__ == '__main__':
    main()
