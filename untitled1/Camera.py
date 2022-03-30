import pyray as pr
class Camera:
    def __init__(self, info) -> None:
        self.camera = pr.Camera3D()
        self.camera.projection = info['projection']
        self.camera.fovy = info['fovy']
        self.camera.position = info['position']
        self.camera.target = info['target']
        self.camera.up = info['up']
        
        print(info['mode'])
        pr.set_camera_mode(self.camera, info['mode'])
