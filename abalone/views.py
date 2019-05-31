import cocos


class MainScene(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        self.bg = Backgroung()
        self.add(self.bg)


class Backgroung(cocos.layer.ColorLayer):
    def __init__(self):
        super().__init__(100, 100, 100, 255)


def main():
    cocos.director.director.init(width=500, height=500)
    scene = views.MainScene()
    cocos.director.director.run(scene)

