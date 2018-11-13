from random import randint; x, n, ans = int(input()), randint(1, 99), {1: '{} > my number', 0: '{} < my number'}
while x != n:
    print(ans[x > n].format(x)); x = int(input())
print('Yay, you guessed it!')
