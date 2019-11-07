from bearlibterminal import terminal as blt

from components.action import Action
from components.control import Control
from components.camera import Camera
from components.physics import Physics
from components.renderable import Renderable

from processors.action_processor import ActionProcessor
from processors.control_processor import ControlProcessor
from processors.camera_processor import CameraProcessor
from processors.physic_processor import PhysicProcessor
from processors.render_processor import RenderProcessor

from utils.esper import World
from utils.layers import Layers


def play_game():
    blt.clear()

    world = World()
    world.create_entity(Action(),
                        Control(),
                        Renderable(char='@', layer=Layers.ENTITIES),
                        Physics(5, 6),
                        Camera(width=20, height=20),
                        name='Player')

    processors = [ControlProcessor, ActionProcessor, PhysicProcessor, CameraProcessor, RenderProcessor]

    for prior, processor in enumerate(processors):
        world.add_processor(processor(), priority=prior)

    world.get_processor(CameraProcessor).get_camera()
    world.get_processor(CameraProcessor).process()

    while True:
        world.process()


if __name__ == '__main__':
    blt.open()
    play_game()
    blt.close()
