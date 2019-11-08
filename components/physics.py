class Physics:
    def __init__(self, pos_x: int = 0, pos_y: int = 0, dest_x: int = 0, dest_y: int = 0, collidable: bool = False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.move: bool = False
        self.movement_cost: int = 3
        self.collidable = collidable
