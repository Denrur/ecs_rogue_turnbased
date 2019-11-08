from components.action import Action
from components.control import Control
from components.physics import Physics

from processors.camera_processor import CameraProcessor

from utils.esper import Processor


class ActionProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        print(f'Action Processor {self.world.timer=}'.center(100, '#'))
        ent = self.current_entity
        print(f'current action entity {ent.name=}')
        action = self.world.component_for_entity(ent, Action)

        if action.type == 'move':
            phys = self.world.component_for_entity(ent, Physics)
            phys.dest_x, phys.dest_y = action.param
            phys.move = action.flag
            action.type = None
        elif action.type == 'change':
            for entity in self.world._entities:
                if entity.name == action.param and entity.name != ent.name:
                    self.world.add_component(entity, Control())
                    self.world.get_processor(CameraProcessor).follow_by(entity)
                    print(f'{ent.name}')
                    self.world.remove_component(ent, Control)
                    break
