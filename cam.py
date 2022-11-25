from vector3 import Vector3
import vars

class Cam(object):
    def __init__(self):
        self.init()
    def init(self):
        self.pos = Vector3(vars.SPACE_WIDTH / 2, vars.SPACE_WIDTH / 2, 0)
cam = Cam()