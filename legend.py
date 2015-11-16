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
        self.vx=0
        self.vy=0
        self.vr=0
        self.scale=.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
class Bullet(Sprite):
    asset = ImageAsset("images/orb-150545_640.png")

    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        self.vx=1
        self.vy=-.5
        self.scale=.1
        self.vr=0

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += .05
        self.rotation += self.vr


class TankGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        tankOne=Tank((200,300))
        Bullet((tankOne.position))

    def step(self):
        for ship in self.getSpritesbyClass(Tank):
            ship.step()
        for ship in self.getSpritesbyClass(Bullet):
            ship.step()


myapp = TankGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
