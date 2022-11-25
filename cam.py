import vector3
import vars

class Cam(object):
    def __init__(self):
        self.pos = vector3.Vector3(vars.SPACE_WIDTH / 2, vars.SPACE_WIDTH / 2, 0)

    def posForRender(self):
        return vector3.Vector3(
            self.pos.x - (vars.WINDOW_WIDTH / 2), 
            self.pos.y - (vars.WINDOW_HEIGHT / 2), 
            self.pos.z 
        )

cam = Cam()