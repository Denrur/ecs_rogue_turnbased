class Renderable:
    def __init__(self, char: str = '@', color='white', pos_x: int = 0, pos_y: int = 0, layer=None):
        self.x = pos_x
        self.y = pos_y
        self.char = char
        self.layer = layer
        self.color = color

