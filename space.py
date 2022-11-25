import vector3
import random
import vars
import pygame
from cam import cam
from math import fabs

class Space(object):
    def __init__(self):
        self.list = [vector3.Vector3(0, 0, 0)] * vars.SPACE_STARS_COUNT
        for i in range(1, vars.SPACE_STARS_COUNT):
            self.list[i] = vector3.Vector3(
                random.randint(1, vars.SPACE_WIDTH), 
                random.randint(1, vars.SPACE_WIDTH), 
                random.randint(1, vars.SPACE_WIDTH)
                )
    def display(self, surface):
        index = 0
        for p in self.list:
            if cam.pos.z < p.z and p.z < cam.pos.z + vars.SPACE_WIDTH:
                dist = vector3.dist(cam.pos, p)
                # distForColor = ((dist + 1) / 200) + 1
                distForColor = int(255 * (vars.SPACE_WIDTH * 1.5 / dist / 15)) - 20
                if distForColor < 0: distForColor = 0
                if distForColor > 255: distForColor = 255

                pX = (vars.WINDOW_WIDTH / 2) + ((p.x - cam.pos.x) / fabs(p.z - cam.pos.z) * 500)
                pY = (vars.WINDOW_HEIGHT / 2) + ((p.y - cam.pos.y) / fabs(p.z - cam.pos.z) * 500)

                pygame.draw.rect(surface, (distForColor, distForColor, distForColor), 
                    (
                        pX, 
                        pY, 
                        3, #10 / (dist / 10), 
                        3, #10 / (dist / 10)
                    ))
            else:
                if cam.pos.z > p.z:
                    self.list[index] = vector3.Vector3(
                        random.randint(1, vars.SPACE_WIDTH), 
                        random.randint(1, vars.SPACE_WIDTH), 
                        cam.pos.z + vars.SPACE_WIDTH
                    )     
                elif p.z > cam.pos.z + vars.SPACE_WIDTH:
                    self.list[index] = vector3.Vector3(
                        random.randint(1, vars.SPACE_WIDTH), 
                        random.randint(1, vars.SPACE_WIDTH), 
                        cam.pos.z
                    )  
            index = index + 1

