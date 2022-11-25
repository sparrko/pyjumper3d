from vector3 import Vector3, dist
import random
import vars
import pygame
from cam import cam
from math import fabs

class Planes(object):
    def __init__(self):
        self.list = [Vector3(0, 0, 0)] * vars.PLANE_COUNT
        for i in range(1, vars.PLANE_COUNT):
            self.list[i] = Vector3(
                random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                random.randint(1, vars.GAMEZONE_WIDTH)
                )
        # Стартовые платформы в форме плюса
        self.list[0] = Vector3(vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, 500)
        fixMove = 5
        self.list[1] = Vector3(vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2 + vars.PLANE_WIDTH - fixMove, vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, 500)
        self.list[2] = Vector3(vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2 - vars.PLANE_WIDTH + fixMove, vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, 500)
        self.list[3] = Vector3(vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2 + vars.PLANE_WIDTH - fixMove, 500)
        self.list[4] = Vector3(vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2, vars.SPACE_WIDTH / 2 - vars.PLANE_WIDTH / 2 - vars.PLANE_WIDTH + fixMove, 500)
        self.list.sort(key=lambda x: x.z, reverse=True)
    def display(self, surface):
        index = 0
        for p in self.list:
            if cam.pos.z < p.z and p.z < cam.pos.z + vars.GAMEZONE_WIDTH:
                distForColor = int(255 * (vars.GAMEZONE_WIDTH * 1.5 / dist(cam.pos, p) / 15)) - 20
                if distForColor < 0: distForColor = 0
                if distForColor > 255: distForColor = 255

                pX = (vars.WINDOW_WIDTH / 2) + ((p.x - cam.pos.x) / fabs(p.z - cam.pos.z) * vars.WINDOW_HEIGHT)
                pY = (vars.WINDOW_HEIGHT / 2) + ((p.y - cam.pos.y) / fabs(p.z - cam.pos.z) * vars.WINDOW_HEIGHT)
                pXw = (vars.WINDOW_WIDTH / 2) + (((p.x + vars.PLANE_WIDTH) - cam.pos.x) / fabs(p.z - cam.pos.z) * vars.WINDOW_HEIGHT) - pX
                pYw = (vars.WINDOW_HEIGHT / 2) + (((p.y + vars.PLANE_WIDTH) - cam.pos.y) / fabs(p.z - cam.pos.z) * vars.WINDOW_HEIGHT) - pY

                color = [distForColor, distForColor, distForColor]

                pygame.draw.rect(surface, color, (pX, pY, pXw, pYw))
            else:
                if p.z > cam.pos.z + vars.GAMEZONE_WIDTH:
                    self.list.pop(index)
                    self.list.insert(vars.PLANE_COUNT - 1, Vector3(
                        random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                        random.randint((vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2), (vars.SPACE_WIDTH / 2 - vars.GAMEZONE_WIDTH / 2) + vars.GAMEZONE_WIDTH), 
                        cam.pos.z
                    ))
            index = index + 1

