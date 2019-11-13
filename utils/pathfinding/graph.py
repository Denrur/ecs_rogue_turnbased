from utils.decorators import benchmark


class GridWithWeights:
    def __init__(self, start, obstacle, size):
        self.start = start
        self.size = size
        self.weights = dict()
        self.obstacle = obstacle
        self.edges = self.make_graph(size)

    @benchmark
    def make_graph(self,size):
        edges = dict()
        for x in range(self.start[0] - size, self.start[0] + size):
            for y in range(self.start[1] - size, self.start[1] + size):
                if (x, y) not in self.obstacle:
                    edges[(x, y)] = self.neighbors((x, y))

        return edges

    def in_bounds(self, loc):
        (x, y) = loc
        return (self.start[0] - self.size <= x <= self.start[0] + self.size and
                self.start[1] - self.size <= y <= self.start[1] + self.size)

    # def passable(self, loc):
    #     return loc not in self.obstacle

    # @benchmark
    def neighbors(self, loc):
        (x, y) = loc
        neighbors = list()

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbors.append((x + i, y + j))
                if abs(i) == abs(j):
                    self.weights[(x + i, y + j)] = 1.41
                else:
                    self.weights[(x + i, y + j)] = 1
        neighbors = list(filter(self.in_bounds, neighbors))
        # neighbors = list(filter(self.passable, neighbors))
        return neighbors

    # def cost(self, from_node, to_node):
    #     return self.weights.get(to_node, 1)
    #
    # def rescan_map(self):
    #     self.obstacle = [(pos.x, pos.y) for ent, pos in self.world.get_component(Position) if
    #                      self.world.component_for_entity(ent, Physics).collidable]

