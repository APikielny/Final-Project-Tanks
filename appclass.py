"""
Final Project
Adam Pikielny
Roger Danilek
Tank Game
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from tank import Tank1, Tank2
from bullet import Bullet, Explosion
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class TankGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0x000000, 1)
        noline = LineStyle(1, black)
        mtn = RectangleAsset(50,150,noline,Color(0x074a36,1.0))
        self.mtn = Sprite(mtn, (270,200))
        bg = RectangleAsset(700,100,noline,Color(0x074a36,1.0))
        #bg=PolygonAsset([(0,0),(700,0),(700,200),(0,200),(0,0)],noline,Color(0x074a36,1.0))
        self.bg=Sprite(bg, (0,300))
        tankOne=Tank1((random.randint(20,150),265))
        tankTwo=Tank2((random.randint(350,500),265))
        lol=input("This is the position of tank 1. Press return to continue with firing of Tank 1." + str(tankOne.position))
        bulletOne=Bullet((tankOne.position),self)
        amirite=input("This is the position of tank 2. Press return to continue with firing of Tank 2." + str(tankTwo.position))
        bulletTwo=Bullet((tankTwo.position),self)
        
        
    def step(self):
        for ship in self.getSpritesbyClass(Tank1):
            ship.step()
        for ship in self.getSpritesbyClass(Tank2):
            ship.step()
        for ship in self.getSpritesbyClass(Bullet):
            ship.step()
        for ship in self.getSpritesbyClass(Explosion):
            ship.step()
            
myapp = TankGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
