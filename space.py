from vector3 import Vector3, dist
import random
import vars
import pygame
from cam import cam
from math import fabs, sin, cos

class Space(object):
    def __init__(self):
        self.list = [Vector3(0, 0, 0)] * vars.SPACE_STARS_COUNT
        for i in range(0, int(vars.SPACE_STARS_COUNT / 2)):
            self.list[i] = Vector3(random.randint(0, vars.SPACE_WIDTH), random.randint(0, vars.SPACE_WIDTH), random.randint(0, vars.SPACE_WIDTH))

        # Завитулька
        vZav = Vector3(vars.SPACE_WIDTH / 2, vars.SPACE_WIDTH / 2, 1000)
        zavSize = 1000
        i = 0.0
        index = int(vars.SPACE_STARS_COUNT / 2)
        while index < vars.SPACE_STARS_COUNT:
            self.list[index] = Vector3(vZav.x + sin(i) * zavSize, vZav.y + cos(i) * zavSize, vZav.z + i * zavSize)
            i += 0.05
            index += 1

    def display(self, surface):
        index = 0
        for p in self.list:
            if cam.pos.z < p.z and p.z < cam.pos.z + vars.SPACE_WIDTH:
                distForColor = int(255 * (vars.SPACE_WIDTH * 1.5 / dist(cam.pos, p) / 15)) - 20
                if distForColor < 0: distForColor = 0
                elif distForColor > 255: distForColor = 255

                pX = (vars.WINDOW_WIDTH / 2) + ((p.x - cam.pos.x) / fabs(p.z - cam.pos.z) * vars.WINDOW_HEIGHT)
                pY = (vars.WINDOW_HEIGHT / 2) + ((p.y - cam.pos.y) / fabs(p.z - cam.pos.z) * vars.WINDOW_HEIGHT)

                pygame.draw.rect(surface, (distForColor, distForColor, distForColor), (pX, pY, 3, 3,))
            else:
                if cam.pos.z > p.z:
                    self.list[index] = Vector3(
                        random.randint(1, vars.SPACE_WIDTH), 
                        random.randint(1, vars.SPACE_WIDTH), 
                        cam.pos.z + vars.SPACE_WIDTH
                    )     
                elif p.z > cam.pos.z + vars.SPACE_WIDTH:
                    self.list[index] = Vector3(
                        random.randint(1, vars.SPACE_WIDTH), 
                        random.randint(1, vars.SPACE_WIDTH), 
                        cam.pos.z
                    )  
            index = index + 1

