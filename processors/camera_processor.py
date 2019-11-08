from components.camera import Camera
from components.physics import Physics
from components.renderable import Renderable

from utils.esper import Processor


class CameraProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.camera = None

    def process(self, *args, **kwargs):
        followed_entity = self.camera.lock_to_char
        if followed_entity:
            phys = self.world.component_for_entity(followed_entity, Physics)
            self.move_camera(phys.pos_x, phys.pos_y)
        for ent, (rend, phys) in self.world.get_components(Renderable, Physics):
            rend.rend_x, rend.rend_y = self.to_camera_coordinates(phys.pos_x, phys.pos_y)

    def get_camera(self):
        for ent, cam in self.world.get_component(Camera):
            self.camera = cam

    def follow_by(self, ent):
        if self.camera:
            self.camera.lock_to_char = ent

    def to_camera_coordinates(self, x, y):
        return x - self.camera.cam_x, y - self.camera.cam_y

    def move_camera(self, x, y):
        # Двигаем камеру к заданным координатам
        self.camera.cam_x = int(x - self.camera.width / 2)
        self.camera.cam_y = int(y - self.camera.height / 2)
