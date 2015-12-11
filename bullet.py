from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from tank import Tank
import math

 
class Bullet(Sprite):
    asset = ImageAsset("images/300px-BM_Grenade.png", Frame(100,20,100,115), 1, 'vertical')
    asset2 = ImageAsset("images/GrenadeExplosion.png", Frame(0,0,51.2,128), 20, 'horizontal')

    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        t = 1.57
        V = 4
        self.vx=V*math.cos(t)
        self.vy=-V*math.sin(t)
        self.scale=.5
        self.vr=0
        self.fxcenter = .5
        self.fycenter = .5
        self.away = False
        self.explode = True
        self.explodeframe = 1


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += .05
        self.rotation += .1
        colliding = self.collidingWithSprites(Tank)
        if colliding and self.away == True:  
            self.setImage(self.explodeframe)
            self.explodeframe += 1
            if self.explodeframe == 20:
                self.explodeframe = 1
        elif not colliding and self.away == False:
            self.away = True
