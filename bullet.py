from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from tank import Tank
import math

 
class Bullet(Sprite):
    asset = ImageAsset("images/300px-BM_Grenade.png", Frame(100,20,100,115), 1, 'vertical')

    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        t = .95
        V = 4
        self.vx=V*math.cos(t)
        self.vy=-V*math.sin(t)
        self.scale=.5
        self.vr=0
        self.fxcenter = .5
        self.fycenter = .5
        self.away = True


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += .005
        self.rotation += .1
        #if self.collidingWithSprites(Tank):  
            #print("COLLIDING")
            #if self.away == True:
                #print("AWAY")
                #self.away = False
        #elif self.away == False:
            #print("NOT AWAY")
            #self.destroy()
