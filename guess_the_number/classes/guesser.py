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


class ComputerRiddlerHard(Riddler):
    def __init__(self):
        self.borders = {'left':1, 'right':100}

    def check(self, guessed_number):
        if self.borders['left'] <= guessed_number <= self.borders['right']:
            if self.borders['left'] == self.borders['right']:
                return True, '='
            elif guessed_number - self.borders['left'] <= self.borders['right'] - guessed_number:
                self.borders['left'] = guessed_number + 1
                return False, '>'
            elif guessed_number - self.borders['left'] > self.borders['right'] - guessed_number:
                self.borders['right'] = guessed_number - 1
                return False, '<'
        elif guessed_number <= self.borders['left']:
            return False, '<'
        else:
            return False, '>'


class HumanRiddler(Riddler):
    def check(self, guessed_number):
        phrase = 'Ваше число {}? (> / < / =) '
        ans = input(phrase.format(guessed_number))
        if ans == '=':
            return True, '='
        else:
            return False, ans


class ComputerGuesser(Guesser):
    def __init__(self):
        self.borders = {'left': 1, 'right': 100}

    def guess(self):
        return (self.borders['left'] + self.borders['right']) // 2

    def update(self, reply):
        m = (self.borders['left'] + self.borders['right']) // 2
        if reply == '>':
            self.borders['left'] = m
        elif reply == '<':
            self.borders['right'] = m


class game:
    def __init__(self):
        self.guessed = False
        guesser = int(input('Вы будете отгадывать или загадывать? (1 -- отгадывать, 2 -- загадывать) '))
        types_game = {1:{'guesser':'human', 'riddler':'computer'}, 2:{'guesser':'computer', 'riddler': 'human'}}
        self.settings = types_game[guesser]
        if guesser == 1:
            self.guesser = HumanGuesser()
            difficulte = int(input("сложность: 1 -- просто, 2 -- сложно "))
            if difficulte == 1:
                self.riddler = ComputerRiddler()
            else:
                self.riddler = ComputerRiddlerHard()
        else:
            self.guesser = ComputerGuesser()
            self.riddler = HumanRiddler()

    def voice_out(self, reply):
        if self.settings['guesser'] == 'human':
            if reply == '=':
                print('вы угадали!')
            elif reply == '>':
                print('мое число больше!')
            elif reply == '<':
                print('мое число меньше!')
            else:
                print('error!')
        else:
            self.guesser.update(reply)

    def start_game(self):
        while not self.guessed:
            guessed_number = self.guesser.guess()
            self.guessed, reply = self.riddler.check(guessed_number)
            self.voice_out(reply)

if __name__=='__main__':
    game = game()
    game.start_game()
