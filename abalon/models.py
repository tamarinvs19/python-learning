from itertools import combinations_with_replacement



def f(i, j):
    return list(set([(i, j), (-i, j), (i, -j), (-i, -j), (j, i), (-j, i), (j, -i), (-j, -i)]))


class Field:
    def __init__(self):
        self.start_positions = [(2, 2)]

        self.putts = {(x, y): Putt(x, y)
                for i, j in combinations_with_replacement(range(5), 2) for x, y in f(i, j) if abs(x - y) <= 4}

        self.balls = {
                'white': [Ball(self.putts[(x, y)], 'white') for (x, y) in self.start_positions],
                'black': [Ball(self.putts[(-x, -y)], 'black') for (x, y) in self.start_positions]
                }


class Hexagonal_position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def euclidean_coordinates(self):
        return self.x * 0.5, self.y * 3**0.5 * 0.5


class Putt:
    def __init__(self, x, y):
        self.position = Hexagonal_position(x, y)
        
    @property
    def possible_steps(self):
        x, y = self.position.x, self.position.y
        return [(x+i, y+j) for i in {1, -1} for j in {1, -1} if abs(x+i) <= 4 and abs(y+j) <= 4 and abs(x+i-y-j) <= 4]


class Ball:
    def __init__(self, putt, color):
        self.putt = putt
        self.color = color
        self.field = None


if __name__ ==  '__main__':
    field = Field()
