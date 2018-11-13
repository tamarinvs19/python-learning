from random import randint


def game_guesser():
    l = 0
    r = 100
    while l + 1 < r:
        m = (l + r)//2
        print ("Your number > " + str(m) + '?')
        if input() in {'1', 'True', 'Yes', 'YES', 'y'}:
            l = m
        else:
            r = m
    print('Is your number', r, '?')
    if input() in {'YES', 'Yes', 'yes', 'y', '1'}:
        print('Yey, I am very good gamer!')
    else:
        print('You are cheating!!')

def game_lite_thinking(n):
    x = int(input())
    ans = {1: '{} > my number', 0: '{} < my number'}
    while x != n:
        print(ans[x > n].format(x))
        x = int(input())
    print('Yey, you guessed my number!')

def game_hard_thinking():
    l, r = 1, 99
    while l != r:
        x = int(input())
        if l < x < r and x - l >= r - x:
            print(x, '> my number')
            r = x - 1
        elif l < x < r and x - l < r - x:
            print(x, '< my number')
            l = x + 1
        elif x > r:
            print(x, '> my number')
        elif x < l:
            print(x, '< my number')
        elif x == r:
            print(x, '> my number')
            r -= 1
        elif x == l:
            print(x, '< my number')
            l += 1
    game_lite_thinking(r)

def main():
    print('Hello!\nChoose the type of game\n(1 : You are guesser, 2 : I am guesser)')
    if int(input()) == 1:
        print('What difficulty level do you want?\n(1 : lite, 2 : hard)')
        if int(input()) == 1:
            game_lite_thinking(randint(1, 99))
        else:
            game_hard_thinking()
    else:
        game_guesser()
main()
