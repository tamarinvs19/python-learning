import random


class Guesser:
    def guess(self, guessed_number):
        raise NotImplementError


class Riddler:
    def check(self, guessed_number):
        raise NotImplementError
   

class HumanGuesser(Guesser):
    def guess(self):
        return int(input('Предположите: '))


class ComputerRiddler(Riddler):
    def __init__(self):
        self.number = random.randint(1, 99)

    def check(self, guessed_number):
        if guessed_number == self.number:
            return True, '='
        elif self.number > guessed_number:
            return False, '>'
        else:
            return False, '<'


class game:
    def __init__(self):
        self.guessed = false
        self.guesser = HumanGuesser()
        difficulte = int(input("сложность: 1 -- просто, 2 -- сложно "))
        if difficulte == 1:
            self.riddler = ComputerRiddler()
        else:
            self.riddler = ComputerRiddlerHard()
        self.riddler = ComputerRiddler()
    
    def voice_out(self, reply):
        if reply == '=':
            print('вы угадали!')
        elif reply == '>':
            print('мое число больше!')
        elif reply == '<':
            print('мое число меньше!')
        else:
            print('error!')

    def start_game(self):
        while not self.guessed:
            guessed_number = self.guesser.guess()
            self.guessed, reply = self.riddler.check(guessed_number)
            self.voice_out(reply)

if __name__=='__main__':
    game = game()
    game.start_game()
