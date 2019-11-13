from components.damager import Damager
from components.physics import Physics

from utils.esper import Processor


class PhysicProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        print(f'Physic processor'.center(100, '#'))
        ent = self.current_entity

        phys = self.world.component_for_entity(ent, Physics)
        dmg = self.world.component_for_entity(ent, Damager)
        if phys.move:
            destination = (phys.pos_x + phys.dest_x, phys.pos_y + phys.dest_y)
            target_list = self.world.entities_position[destination]
            if not target_list[1].value:
                self.change_position(phys, ent)

        if dmg.attack:
            destination = (phys.pos_x + dmg.dest_x, phys.pos_y + dmg.dest_y)
            target_list = self.world.entities_position[destination]
            print(f'Attack with {dmg.power=}')
            for target in target_list[0]:
                print(f'{target=}')
                if target:
                    target_phys = self.world.component_for_entity(target, Physics)
                    target_phys.health -= dmg.power
                    if target_phys.health <= 0:
                        self.kill_entity(target, target_list)

    def change_position(self, phys, ent):
        self.world.entities_position[(phys.pos_x, phys.pos_y)][0].remove(ent)
        self.world.entities_position[(phys.pos_x, phys.pos_y)][1] -= phys.collidable
        if not self.world.entities_position[(phys.pos_x, phys.pos_y)][0]:
            del self.world.entities_position[(phys.pos_x, phys.pos_y)]
        phys.pos_x += phys.dest_x
        phys.pos_y += phys.dest_y
        self.world.entities_position[(phys.pos_x, phys.pos_y)][0].append(ent)
        self.world.entities_position[(phys.pos_x, phys.pos_y)][1] += phys.collidable
        phys.move = False

    def kill_entity(self, ent, list_of_entities):
        list_of_entities[0].remove(ent)
        list_of_entities[1] = False
        self.world.delete_entity(ent, immediate=True)
