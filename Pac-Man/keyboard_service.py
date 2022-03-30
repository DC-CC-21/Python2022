import pyray as pr

class Keyboard:
    def __init__(self):
        self.keys = {}
        self.keys['w'] = pr.KEY_W
        self.keys['a'] = pr.KEY_A
        self.keys['s'] = pr.KEY_S
        self.keys['d'] = pr.KEY_D

    def is_pressed(self, key):
        return pr.is_key_pressed(self.keys[key])