from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Tank1(Sprite):
    asset = ImageAsset("images/medium_tank_by_skorpion66-d6fdave.png")
    def __init__(self, position):
        super().__init__(Tank1.asset, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.scale=.06
        #TankGame.listenKeyEvent("keydown", "left arrow", self.moveleft)
        print("test")
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr

    """def moveleft(self,event):
        self.vx+=.5"""
        
class Tank2(Sprite):
    asset = ImageAsset("images/tanks_by_fvsj-d6if9gt.png", Frame(100,550,350,160), 1, 'vertical')
    def __init__(self, position):
        super().__init__(Tank2.asset, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.scale=.25
        #TankGame.listenKeyEvent("keydown", "left arrow", self.moveleft)
        print("test")
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr

    """def moveleft(self,event):
        self.vx+=.5"""
        
