class Physics:
    def __init__(self, x: int = 0, y: int = 0, dest_x: int = 0, dest_y: int = 0, collidable: bool = False):
        self.x = x
        self.y = y
        self.dest_x: int = dest_x
        self.dest_y: int = dest_y
        self.move: bool = False
        self.movement_cost: int = 3
        self.collidable = collidable
