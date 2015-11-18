class Tank(Sprite):
    from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

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
