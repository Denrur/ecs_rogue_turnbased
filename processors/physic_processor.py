from components.action import Action
from components.physics import Physics

from processors.action_processor import ActionProcessor

from utils.esper import Processor


class PhysicProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        print(f'Physic processor'.center(100, '#'))
        ent = self.world.get_processor(ActionProcessor).current_entity
        action = self.world.component_for_entity(ent, Action)

        phys = self.world.component_for_entity(ent, Physics)

        print(f'''{ent.name=}, {action.type=}, {action.cost=}, {phys.x=}, {phys.y=},
        {phys.dest_x=}, {phys.dest_y=}''')
        if action.type == 'move':
            move(phys)


def move(phys):
    phys.x += phys.dest_x
    phys.y += phys.dest_y
    phys.dest_x = 0
    phys.dest_y = 0
    phys.move = False
