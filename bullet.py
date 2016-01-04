from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from tank import Tank1, Tank2
#from appclass import myapp
import math

class Bullet(Sprite):
    asset = ImageAsset("images/300px-BM_Grenade.png", Frame(100,20,100,115), 1, 'vertical')

    def __init__(self, position, app):
        super().__init__(Bullet.asset, position)
        self.scale=.25
        self.vr=0
        self.fxcenter = .5
        self.fycenter = .5
        self.away = False
        self.asked= False
        self.app=app
        if self.asked==False:
            t=int(input("Input an angle, in degrees, between 0 and 180. 0 is due east."))*(math.pi/180)
            V=int(input("Input a magnitude. This should be a number between 1 and 5."))
            self.vx=V*math.cos(t)
            self.vy=-V*math.sin(t)
            self.asked=True

    def step(self):
        #if self.asked==False:
            """lol=input("This is the first tank's position. Press return.")
            lmfao=input(tankOne.position + "Press return.")
            dab=input("This is the second tank's position. Press return.")
            gnar=input(tankTwo.position + "Press return.")
            n00b=input("There is a wall in the middle. It is 100px high. Press return.")"""
            #t=int(input("Input an angle, in degrees, between 0 and 180. 0 is due east."))*(math.pi/180)
            #V=int(input("Input a magnitude. This should be a number between 1 and 5."))
            #self.vx=V*math.cos(t)
            #self.vy=-V*math.sin(t)
            #self.asked=True
        self.x += self.vx
        self.y += self.vy
        self.vy += .05
        self.rotation += .1
        tanklist=self.collidingWithSprites(Tank1)
        tanklist.extend(self.collidingWithSprites(Tank2))
        if tanklist or self.collidingWith(self.app.bg) or self.collidingWith(self.app.mtn):
            colliding = True
        else:
            colliding = False
        if colliding and self.away == True:
            for tank in tanklist:
                tank.destroy()
            self.vx=0
            self.vy=0
            self.rotation=0
            Explosion(self.position)
            self.destroy()
        elif not colliding and self.away == False:
            self.away = True
   
                
class Explosion(Sprite):
    asset = ImageAsset("images/GrenadeExplosion.png", Frame(0,0,50,128), 20, 'horizontal')
    
    def __init__(self,position):
        super().__init__(Explosion.asset, position)
        self.Explosion = 0
        self.Explosionframe = 1
        
    def step(self):
        self.setImage(self.Explosionframe)
        self.Explosionframe += 1
        if self.Explosionframe == 20:
            self.destroy()
        
