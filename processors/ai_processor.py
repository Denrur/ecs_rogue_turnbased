from utils.esper import Processor
from components.ai import Ai
from components.physics import Physics
from random import random

from processors.map_processor import MapProcessor

from utils.pathfinding.a_star_search import a_star_search
from utils.pathfinding.dijkstra import reconstruct_path
from utils.pathfinding.graph import GridWithWeights


class AiProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.phys = None
        self.target_phys = None
        self.destination = None

    def process(self, *args, **kwargs):
        pass

    def typical_ai(self, entity, target):
        self.phys = self.world.component_for_entity(entity, Physics)
        self.target_phys = self.world.component_for_entity(target, Physics)
        damage = entity.damage
        ai = entity.ai
        charge_probability = random()
        retreat_probability = random()
        if damage > ai.morale:
            if self.can_run_away_from_target(target):
                self.run_away_from_target(target)

            elif self.can_attack_target(target):
                self.attack_target(target)

        elif (self.too_far_from_target(target) and
              self.can_attack_target(target) and
              self.can_move_toward_target(target)):
            if random() < charge_probability:
                self.move_toward_target(target)
            else:
                self.attack_target(target)

        elif (self.too_close_to_target(target) and
              self.can_attack_target(target) and
              self.can_move_away_from_target(target)):
            if random() < retreat_probability:
                self.move_away_from_target(target)
            else:
                self.attack_target(target)

        elif self.can_attack_target(target):
            self.attack_target(target)

        elif (self.too_far_from_target(target) and
              self.can_move_toward_target(target)):
            self.move_toward_target(target)

        elif (self.too_close_to_target(target) and
              self.can_move_away_from_target(target)):
            self.move_away_from_target(target)

        else:
            self.stand_still()

    def can_move_toward_target(self, target):
        start = (self.phys.pos_x, self.phys.pos_y)
        goal = (self.target_phys.pos_x, self.target_phys.pos_y)
        size = 10
        obstacles = self.world.get_processor(MapProcessor).get_obstacles_map(start, size)
        graph = GridWithWeights(start, obstacles, size)
        came_from, cost_so_far = a_star_search(graph, start, goal)
        path = reconstruct_path(came_from, start, goal)
        dest = path.pop(0)
        if dest:
            self.destination = dest
        else:
            return False

    def move_toward_target(self):
        self.phys.dest_x += self.destination[0]
        self.phys.dest_y += self.destination[1]

    def can_move_away_from_target(self, target):
        pass

    def move_away_from_target(self, target):
        pass

    def can_run_away_from_target(self, target):
        pass

    def run_away_from_target(self, target):
        pass

    def too_far_from_target(self, target):
        pass

    def too_close_to_target(self, target):
        pass

    def can_attack_target(self, target):
        pass

    def attack_target(self, target):
        pass

    def stand_still(self):
        pass
