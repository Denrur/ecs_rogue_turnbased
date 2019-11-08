from bearlibterminal import terminal as blt

from components.action import Action
from components.control import Control

from utils.esper import Processor


def handle_keys(ctrl):
    return ctrl.controls.get(ctrl.key)


class ControlProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        print(f'Control processor'.center(100, '#'))
        for ent, ctrl in self.world.get_component(Control):
            print(f'Controled {ent.name=}')
            self.world.current_entity = ent
            ctrl.key = blt.read()
            action = self.world.component_for_entity(ent, Action)
            act = handle_keys(ctrl)
            print(act)
            if act:
                for action_type, action_param in act.items():
                    action.type, action.param = action_type, action_param
                    action.flag = True



