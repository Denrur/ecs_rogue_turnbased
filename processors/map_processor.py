from utils.esper import Processor


class MapProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        pass

    def get_obstacles_map(self, start, size):
        x, y = start
        return [c for c, v in self.world.entities_position.items() if v[1] and
                (x - size <= c[0] <= x + size and y - size <= c[1] <= y + size)]
