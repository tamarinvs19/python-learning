import cocos
import views, models


class MainScene(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        self.bg = Backgroung()
        self.field = models.Field()
        self.add(self.bg)
        self.add(self.field)


class Backgroung(cocos.layer.ColorLayer):
    def __init__(self):
        super().__init__(100, 100, 100, 255)


def main():
    cocos.director.director.init(width=500, height=500)
    scene = MainScene()
    cocos.director.director.run(scene)

