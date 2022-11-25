import vector3
import random
import vars
import pygame
from cam import cam
from math import fabs

class Planes(object):
    def __init__(self):
        self.list = [vector3.Vector3(0, 0, 0)] * vars.PLANE_COUNT
        for i in range(1, vars.PLANE_COUNT):
            self.list[i] = vector3.Vector3(
                random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                random.randint(1, vars.GAMEZONE_WIDTH)
                )
        self.list[0] = vector3.Vector3(
            vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, 
            vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, 
            500
        )
        self.list.sort(key=lambda x: x.z, reverse=True)
    def display(self, surface, trigPlane = -1):
        index = 0
        for p in self.list:
            if cam.pos.z < p.z and p.z < cam.pos.z + vars.GAMEZONE_WIDTH:
                dist = vector3.dist(cam.pos, p)
                # distForColor = ((dist + 1) / 200) + 1
                distForColor = int(255 * (vars.GAMEZONE_WIDTH * 1.5 / dist / 15)) - 20
                if distForColor < 0: distForColor = 0
                if distForColor > 255: distForColor = 255

                pX = (vars.WINDOW_WIDTH / 2) + ((p.x - cam.pos.x) / fabs(p.z - cam.pos.z) * 1000)
                pY = (vars.WINDOW_HEIGHT / 2) + ((p.y - cam.pos.y) / fabs(p.z - cam.pos.z) * 1000)
                pXw = (vars.WINDOW_WIDTH / 2) + (((p.x + vars.PLANE_WIDTH) - cam.pos.x) / fabs(p.z - cam.pos.z) * 1000) - pX
                pYw = (vars.WINDOW_HEIGHT / 2) + (((p.y + vars.PLANE_WIDTH) - cam.pos.y) / fabs(p.z - cam.pos.z) * 1000) - pY


                if trigPlane == index: color = [distForColor, 0, 0]
                else: color = [distForColor, distForColor, distForColor]

                pygame.draw.rect(surface, color, 
                    (
                        pX, 
                        pY, 
                        pXw, #10 / (dist / 10), 
                        pYw, #10 / (dist / 10)
                    ))
            else:
                if p.z > cam.pos.z + vars.GAMEZONE_WIDTH:
                    self.list.pop(index)
                    self.list.insert(vars.PLANE_COUNT - 1, vector3.Vector3(
                        random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                        random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                        cam.pos.z
                    ))
            index = index + 1

