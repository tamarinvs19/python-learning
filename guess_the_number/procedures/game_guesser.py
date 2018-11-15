from communication import guess, print_out

def update(l, r, m, ans):
    if ans in {'1', 'True', 'Yes', 'YES', 'y'}:
        l = m
    else:
        r = m
    return l, r

def game_guesser():
    l = 0
    r = 100
    while l + 1 < r:
        m = (l + r)//2
        ans = guess('Answer: ', "Your number > " + str(m) + '?', str)
        l, r = update(l, r, m, ans)
    if guess('Answer: ', 'Is your number ' + str(r) + '?', str) in {'YES', 'Yes', 'yes', 'y', '1'}:
        print_out('Yey, I am very good gamer!')
    else:
        print_out('You are cheating!!')

if __name__ == "__main__":
    game_guesser()
