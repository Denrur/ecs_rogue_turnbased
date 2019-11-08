from components.physics import Physics

from utils.esper import Processor


class PhysicProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        print(f'Physic processor'.center(100, '#'))
        ent = self.current_entity

        phys = self.world.component_for_entity(ent, Physics)

        if phys.move:
            destination = (phys.pos_x + phys.dest_x, phys.pos_y + phys.dest_y)
            if self.world.entities_position[destination][1]:
                self.change_position(phys, ent)

    def change_position(self, phys, ent):
        self.world.entities_position[(phys.pos_x, phys.pos_y)][0].remove(ent)
        self.world.entities_position[(phys.pos_x, phys.pos_y)][1] = True
        if not self.world.entities_position[(phys.pos_x, phys.pos_y)][0]:
            del self.world.entities_position[(phys.pos_x, phys.pos_y)]
        phys.pos_x += phys.dest_x
        phys.pos_y += phys.dest_y
        self.world.entities_position[(phys.pos_x, phys.pos_y)][0].append(ent)
        self.world.entities_position[(phys.pos_x, phys.pos_y)][1] = False
        phys.move = False
