from components.action import Action
from components.physics import Physics

from utils.esper import Processor


class ActionProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.current_entity = None

    def process(self):
        print(f'Action Processor {self.world.timer=}'.center(100, '#'))

        action = self.world.component_for_entity(self.current_entity, Action)

        if action.type == 'move':
            phys = self.world.component_for_entity(self.current_entity, Physics)
            phys.x, phys.y = action.param
            phys.move = action.flag