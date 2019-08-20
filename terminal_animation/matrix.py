from random import randint
from time import sleep


y = 1
def f(x):
    global y
    y = (y + 10) % 239
    return (y%139)**2 + 2*(x%120)**2 +5

def main():
    # for i in range(100):
    while True:
        ls = [f(x) % 4 for x in range(100)]
        print(''.join(map(lambda x: ' ' if x != 0 else str(1), ls)))
        sleep(0.1)


if __name__ == '__main__':
    main()
