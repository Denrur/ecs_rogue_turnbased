from utils.bool_operation import Blocked


class Physics:
    def __init__(self):
        self.health: int = 0
        self.pos_x: int = 0
        self.pos_y: int = 0
        self.dest_x: int = 0
        self.dest_y: int = 0
        self.move: bool = False
        self.movement_cost: int = 3
        self.collidable = Blocked(False)
