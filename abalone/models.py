from pprint import pprint
from itertools import combinations_with_replacement
import cocos
from pyglet.window import key



def f(i, j):
    return list(set([(i, j), (-i, j), (i, -j), (-i, -j), (j, i), (-j, i), (j, -i), (-j, -i)]))


class Field(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        self.start_positions = [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4),
                (-1, 4), (0, 3), (1, 2), (2, 1), (3, 0), (4, -1),
                (0, 2), (1, 1), (2, 0)]

        self.putts = {(x, y): Putt(x, y)
                for i, j in combinations_with_replacement(range(5), 2) for x, y in f(i, j) if abs(x + y) <= 4}

        self.balls = {
                'white': [Ball(self.putts[(x, y)], 'white') for (x, y) in self.start_positions],
                'black': [Ball(self.putts[(-x, -y)], 'black') for (x, y) in self.start_positions]
                }

        self.activation()

    def activation(self):
        for putt in self.putts.values():
            self.add(putt)
        for ball in self.balls['white']:
            self.add(ball)
        for ball in self.balls['black']:
            self.add(ball)


class Hexagonal_position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def euclidean_coordinates(self):
        return (self.x - self.y) / 2 * 50 + 230, (self.x + self.y) * 3**0.5 / 2 * 50 + 200


class Putt(cocos.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__('pictures/putt.png')
        self.hex_position = Hexagonal_position(x, y)
        self.anchor = self.width/2, self.height/2
        self.position = self.hex_position.euclidean_coordinates
        self.scale = 0.5
        
    @property
    def possible_steps(self):
        x, y = self.position.x, self.position.y
        return [(x+i, y+j) for i in {1, -1} for j in {1, -1} if abs(x+i) <= 4 and abs(y+j) <= 4 and abs(x+i-y-j) <= 4]


class Ball(cocos.sprite.Sprite):
    def __init__(self, putt, color):
        super().__init__('pictures/{}_ball.png'.format(color))
        self.anchor = self.width/2, self.height/2
        self.scale = 0.5
        self.putt = putt

        dx, dy = (self.putt.width - self.width)/2, (self.putt.height - self.height)/2
        self.position = self.putt.position[0] + dx, self.putt.position[1] + dy

        self._color = color


if __name__ ==  '__main__':
    field = Field()
