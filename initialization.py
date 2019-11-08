from add_entities import add_entities

from processors.action_processor import ActionProcessor
from processors.control_processor import ControlProcessor
from processors.camera_processor import CameraProcessor
from processors.physic_processor import PhysicProcessor
from processors.render_processor import RenderProcessor

from utils.esper import World


def init_world():
    world = World()
    player = add_entities(world)

    processors = [ControlProcessor,
                  ActionProcessor,
                  PhysicProcessor,
                  CameraProcessor,
                  RenderProcessor]

    for prior, processor in enumerate(processors):
        world.add_processor(processor(), priority=prior)

    world.get_processor(CameraProcessor).get_camera()
    world.get_processor(CameraProcessor).follow_by(player)
    world.get_processor(CameraProcessor).process()

    return world
