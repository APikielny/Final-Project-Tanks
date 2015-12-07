from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from tank import Tank

 
class Bullet(Sprite):
    asset = ImageAsset("images/300px-BM_Grenade.png", Frame(100,20,100,115), 1, 'vertical')

    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        self.vx=3
        self.vy=-2
        self.scale=.5
        self.vr=0
        self.fxcenter = .5
        self.fycenter = .5
        self.away = True


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += .05
        self.rotation += .1
        if self.collidingWithSprites(Tank):  
            print("COLLIDING")
            if self.away == True:
                print("AWAY")
                self.destroy()
        elif self.away == False:
            print("NOT AWAY")
            self.away = True
