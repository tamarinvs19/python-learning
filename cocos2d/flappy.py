import cocos
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite
from pyglet.window import key
from cocos.actions.interval_actions import Delay
from cocos.actions.instant_actions import CallFunc, Repeat
from math import sin

size, higth_b = (1300, 800), 1000

class Barrier(Sprite):
    def __init__(self, x, h):
        super().__init__('barrier.png')
        self.position = x, h-higth_b//2
        self.h, self.v, self.r = h, 4, 40
        self.schedule(self.phyzic)

    def phyzic(self, dt):
        if not self.parent.pause:
            x, y = self.position
            self.position = x - self.v, y
            if self.position[0] < -40: self.parent.remove(self)


class Badger(Sprite):
    def __init__(self, x, y):
        super().__init__('badger.png')
        self.position = x, y
        self.control_up = key.SPACE
        self.v_up, self.v_down = 10, 2
        self.r = 32

        self.schedule(self.phyzic)

    def move(self, direction):
        check = {'up':lambda x, y: ((x, y + self.v_up), True) if y + self.v_up < self.parent.size[1] else ((x, y), False),
                 'down':lambda x, y: ((x, y - self.v_up), True) if y - self.v_up > 0 else ((x, y), False)}
        self.position, res = check[direction](*self.position)
        if not res: self.parent.end_game()

    def collision(self):
        x, y = self.position
        for barrier in filter(lambda x: x.__class__.__name__ == 'Barrier', self.parent.get_children()):
            x0, y0 = barrier.position
            if abs(x - x0) <= self.r + barrier.r and abs(y - y0) <= self.r + higth_b//2: self.parent.end_game()

    def phyzic(self, dt):
        if not self.parent.pause:
            if self.control_up in self.parent.keys: self.move('up')
            else: self.move('down')
            self.collision()


class Game(Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        self.size = size
        self.count = 0
        self.keys = set()
        self.pause = False

        self.add(Badger(self.size[0]//4, self.size[1]//2))
        self.do(Repeat(Delay(1) + CallFunc(self.creating)))
        self.add(cocos.text.Label(text=str(max(0, self.count-4)), position=(15, self.size[1]//2), font_name='Times New Roman', font_size=32,  anchor_x='left'))

    def end_game(self):
        self.pause = True
        self.add(cocos.text.Label('Game over', position=map(lambda x: x//2, size), font_name='Times New Roman', font_size=64,  anchor_x='center', anchor_y='center'))
        self.add(cocos.text.Label(text='press <Enter> to restart, <Q> to exit', position=(size[0]//2, size[1]//2-60), font_name='Times New Roman', font_size=32,  anchor_x='center', anchor_y='center'))

    def on_key_press(self, symbol, mod):
        if symbol == key.SPACE and not self.pause: self.keys.add(symbol)

    def on_key_release(self, symbol, mod):
        if symbol == key.SPACE and not self.pause: self.keys.remove(symbol)
        elif symbol == key.ENTER: self.restart()
        elif symbol == key.Q: self.exit()

    def add_pair_of_barriers(self, y, h):
        self.add(Barrier(1400, 0 + y))
        self.add(Barrier(1400, higth_b + y + h))

    def creating(self):
        if not self.pause:
            self.count += 1
            self.remove(list(filter(lambda x: x[1].__class__.__name__ == 'Label', self.children))[0][1])
            self.add(cocos.text.Label(text=str(max(0, self.count-4)), position=(15, self.size[1]//2), font_name='Times New Roman', font_size=32,  anchor_x='left'))
            self.add_pair_of_barriers(250 + 70*sin(self.count), 350 - 70*sin(2*self.count**2 + 15))

    def restart(self):
        for _, c in self.children: self.remove(c)
        self.parent.add(Game())

    def exit(self):
        self.parent.on_exit()
    

class Background(Layer):
    def __init__(self):
        super().__init__()
        self.bg = Sprite('background.png')
        self.bg.position = size[0]//2, size[1]//2
        self.add(self.bg)


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.add(Background())
        self.add(Game())

cocos.director.director.init(width=size[0], height=size[1], fullscreen=True)
cocos.director.director.run(GameScene())
