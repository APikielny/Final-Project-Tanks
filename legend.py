"""
Final Project
Adam Pikielny
Roger Danilek
Tank Game
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Tank(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/tanks_by_fvsj-d6if9gt.png", Frame(100,550,350,160), 1, 'vertical')
    def __init__(self, position):
        super().__init__(Tank.asset, position)
        self.vx=3
        self.vy=-5
        self.vr=0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += .1
        self.rotation += self.vr
        
"""class Bullet(Sprite):
    asset = ImageAsset("images/tanks_by_fvsj-d6if9gt.png", Frame(100,550,350,160), 1, 'vertical')

    def __init__(self, position):
        super().__init__(Tank.asset, position)
        self.vx=5
        self.vy=5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        #self.vy-=.5
        self.rotation += self.vr"""


class TankGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Tank((100,100))

    def step(self):
        for ship in self.getSpritesbyClass(Tank):
            ship.step()


myapp = TankGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
