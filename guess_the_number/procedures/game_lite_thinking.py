from communication import guess, print_out
from random import randint
def game_lite_thinking(n):
    x = int(guess('Suggest: '))
    ans = {1: '{} > my number', 0: '{} < my number'}
    while x != n:
        x = int(guess('Suggest: ', ans[x > n].format(x), int))
    print_out('Yey, you guessed my number!')

if __name__ == "__main__":
    game_lite_thinking(randint(1, 99))
