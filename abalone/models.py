from pprint import pprint
from itertools import combinations_with_replacement
import cocos
from cocos.director import director
from pyglet.window import key



def f(i, j):
    return list(set([(i, j), (-i, j), (i, -j), (-i, -j), (j, i), (-j, i), (j, -i), (-j, -i)]))


class Field(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(Field, self).__init__()
        self.start_positions = [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4),
                (-1, 4), (0, 3), (1, 2), (2, 1), (3, 0), (4, -1),
                (0, 2), (1, 1), (2, 0)]

        self.putts = {(x, y): Putt(x, y)
                for i, j in combinations_with_replacement(range(5), 2) for x, y in f(i, j) if abs(x + y) <= 4}

        self.balls = {
                'white': [Ball(self.putts[(x, y)], 'white') for (x, y) in self.start_positions],
                'black': [Ball(self.putts[(-x, -y)], 'black') for (x, y) in self.start_positions]
                }

        self.clicked_balls = set()

        self.activation()


        # mouse and keys
        self.text_mouse = cocos.text.Label('NO', x=0, y=480)
        self.add(self.text_mouse)

        self.text = cocos.text.Label("", x=0, y=460)
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self, x=None, y=None):
        key_names = [key.symbol_string(k) for k in self.keys_pressed]
        text = 'Keys: ' + ', '.join(key_names)
        self.text.element.text = text

    def update_mouse_text(self, x, y):
        text_mouse = str(self.click_mouse(x, y))
        # text_mouse = 'Mouse: {}, {}'.format(x, y)
        self.text_mouse.element.text = text_mouse

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.update_mouse_text(x, y)

    # def on_mouse_drag(self, x, y, dx, dy, buttins, modifiers):
    #     self.update_mouse_text(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.update_mouse_text(x, y)

    def activation(self):
        for putt in self.putts.values():
            self.add(putt)
        for ball in self.balls['white']:
            self.add(ball)
        for ball in self.balls['black']:
            self.add(ball)

    def click_mouse(self, x, y):
        balls = self.balls['white'] + self.balls['black']
        radius = balls[0].height / 2

        collision_balls = [ball for ball in balls if abs(ball.x + radius - x) < radius and abs(ball.y + radius - y) < radius]

        for ball in collision_balls:
            ball.click()

        return collision_balls


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

        self.clicked = [225, 120, 0]

        dx, dy = (self.putt.width - self.width)/2, (self.putt.height - self.height)/2
        self.position = self.putt.position[0] + dx, self.putt.position[1] + dy

        self._color = color

    def click(self):
        if self.color != self.clicked:
            self.parent.clicked_balls.add(self)
            self.color = self.clicked
        else:
            self.color = [255] * 3
            self.parent.clicked_balls.remove(self)


if __name__ ==  '__main__':
    field = Field()
