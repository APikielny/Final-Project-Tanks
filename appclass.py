"""
Final Project
Adam Pikielny
Roger Danilek
Tank Game
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from tank import Tank
from bullet import Bullet, Explosion

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class TankGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg = RectangleAsset(100,700,noline,(0x000000,1.0))
        Sprite(bg, (0,0))
        tankOne=Tank((200,75))
        bulletOne=Bullet((tankOne.position),self)
        #tankTwo=Tank((400,300))
        #bulletTwo=Bullet((tankTwo.position))
        
        
    def step(self):
        for ship in self.getSpritesbyClass(Tank):
            ship.step()
        for ship in self.getSpritesbyClass(Bullet):
            ship.step()
        for ship in self.getSpritesbyClass(Explosion):
            ship.step()
            
myapp = TankGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
