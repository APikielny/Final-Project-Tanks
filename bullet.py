from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Bullet(Sprite):
    asset = ImageAsset("images/300px-BM_Grenade.png", Frame(100,20,100,115), 1, 'vertical')

    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        self.vx=1
        self.vy=-.5
        self.vr=1
        self.scale=.5
        self.vr=0
        self.fxcenter = .5
        self.fycenter = .5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += .05
        self.rotation += .1