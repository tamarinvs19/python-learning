from random import randint
from communication import guess, print_out
from game_guesser import game_guesser
from game_lite_thinking import game_lite_thinking
from game_hard_thinking import game_hard_thinking


def main_thinking():
    print_out('What difficulty level do you want?\n(1 : lite, 2 : hard)')
    if int(input()) == 1:
        game_lite_thinking(randint(1, 99))
    else:
        game_hard_thinking()

def main():
    print_out('Hello!\nChoose the type of game\n(1 : You are guesser, 2 : I am guesser)')
    if int(input()) == 1:
        main_thinking()
    else:
        game_guesser()


if __name__ == "__main__":
    main()
