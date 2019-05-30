import cocos
from . import views, models


def main():
    cocos.director.director.init(width=500, height=500)
    scene = views.MainScene()
    cocos.director.director.run(scene)

    
if __name__ == '__main__':
    main()
