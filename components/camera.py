class Camera:
    def __init__(self, width=20, height=20, cam_x=0, cam_y=0):
        self.width = width
        self.height = height
        self.cam_x = cam_x
        self.cam_y = cam_y
        self.lock_to_char = None
