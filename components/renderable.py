class Renderable:
    def __init__(self, glyph: str = '@', color='white',
                 layer=None, renderable: bool = True):
        self.rend_x = 0
        self.rend_y = 0
        self.glyph = glyph
        self.layer = layer
        self.color = color
        self.renderable = renderable

