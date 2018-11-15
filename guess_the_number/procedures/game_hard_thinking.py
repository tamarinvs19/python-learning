from communication import guess, print_out
from game_lite_thinking import game_lite_thinking


def update(l, r, x):
    if l < x < r and x - l >= r - x:
        print_out(str(x) + ' > my number')
        r = x - 1
    elif l < x < r and x - l < r - x:
        print_out(str(x) + ' < my number')
        l = x + 1
    elif x > r:
        print_out(str(x) + ' > my number')
    elif x < l:
        print_out(str(x) + ' < my number')
    elif x == r:
        print_out(str(x) + ' > my number')
        r -= 1
    elif x == l:
        print_out(str(x) + ' < my number')
        l += 1
    else:
        print_out('Error!!!!')
    return l, r

def game_hard_thinking():
    l, r = 1, 99
    while l != r:
        x = int(guess('Suggest: ', type_var = int))
        l, r = update(l, r, x)
    game_lite_thinking(r)

if __name__ == '__main__':
    game_hard_thinking()
