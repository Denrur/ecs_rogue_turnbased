from bearlibterminal import terminal as blt


class Control:
    def __init__(self):
        self.key = None
        self.controls = {blt.TK_UP: {'move': (0, -1)},
                         blt.TK_DOWN: {'move': (0, 1)},
                         blt.TK_LEFT: {'move': (-1, 0)},
                         blt.TK_RIGHT: {'move': (1, 0)},
                         blt.TK_1:{'change': 'Player'},
                         blt.TK_2:{'change': 'Goblin'},
                         blt.TK_3:{'change': 'Worm'},}
