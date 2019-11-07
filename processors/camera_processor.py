from components.camera import Camera
from components.physics import Physics
from components.renderable import Renderable

from utils.esper import Processor


class CameraProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.camera = None

    def process(self, *args, **kwargs):
        for ent, (rend, pos) in self.world.get_components(Renderable, Physics):
            rend.x, rend.y = self.to_camera_coordinates(pos.x, pos.y)

    def get_camera(self):
        for ent, cam in self.world.get_component(Camera):
            self.camera = cam

    def to_camera_coordinates(self, x, y):
        return x - self.camera.x, y - self.camera.y
