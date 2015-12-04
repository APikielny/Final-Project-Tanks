"""
Final Project
Adam Pikielny
Roger Danilek
Tank Game
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from tank import Tank
from bullet import Bullet

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class TankGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        tankOne=Tank((200,300))
        bulletOne=Bullet((tankOne.position))
        tankTwo=Tank((400,300))
        bulletTwo=Bullet((tankTwo.position))
        
        
    def step(self):
        for ship in self.getSpritesbyClass(Tank):
            ship.step()
        for ship in self.getSpritesbyClass(Bullet):
            ship.step()
            


myapp = TankGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()