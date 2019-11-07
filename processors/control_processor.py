from bearlibterminal import terminal as blt

from components.action import Action
from components.control import Control

from processors.action_processor import ActionProcessor

from utils.esper import Processor


def handle_keys(ctrl):
    if ctrl.controls.get(ctrl.key):
        print(ctrl.controls.get(ctrl.key).items()[0])
    return ctrl.controls.get(ctrl.key)


class ControlProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        for ent, ctrl in self.world.get_component(Control):
            self.world.get_processor(ActionProcessor).current_entity = ent
            ctrl.key = blt.read()
            action = self.world.component_for_entity(ent, Action)
            if handle_keys(ctrl):
                action.type, action.param = handle_keys(ctrl).items()
                action.flag = True

