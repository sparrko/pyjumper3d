from timer import Timer
from space import Space
from planes import Planes
import cam
import pygame
import vars

class Engine():
    def __init__(self):
        self.isRunning = False
        self.timer = Timer()
        self.space = Space()
        self.planes = Planes()
        self.pdz = 0
        self.record = 0

    def init(self):
        pygame.init()
        self.surface = pygame.display.set_mode((vars.WINDOW_WIDTH, vars.WINDOW_HEIGHT))
        self.isRunning = True

    def restart(self):
        self.timer = Timer()
        self.space = Space()
        self.planes = Planes()
        self.pdz = 0
        self.planeIndexTriger = -1
        cam.cam.init()

    def updateEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.isRunning = False
            if event.type == pygame.KEYDOWN:
                pass
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP]:
            cam.cam.pos.y -= vars.PLAYER_SPEEDMOVE
        if self.keys[pygame.K_RIGHT]:
            cam.cam.pos.x += vars.PLAYER_SPEEDMOVE
        if self.keys[pygame.K_DOWN]:
            cam.cam.pos.y += vars.PLAYER_SPEEDMOVE
        if self.keys[pygame.K_LEFT]:
            cam.cam.pos.x -= vars.PLAYER_SPEEDMOVE
        if self.keys[pygame.K_w]:
            cam.cam.pos.z += vars.PLAYER_SPEEDMOVE
        if self.keys[pygame.K_s]:
            cam.cam.pos.z -= vars.PLAYER_SPEEDMOVE
        
        

    def updateLogic(self):
        # Физика колизии
        self.pdz = self.pdz + vars.PLAYER_GRAV
        if self.pdz > vars.PLAYER_MAX_DY: self.restart()
        cam.cam.pos.z = cam.cam.pos.z + self.pdz
        if self.pdz > 0:
            index = 0
            for p in self.planes.list:
                if p.z - cam.cam.pos.z < vars.PLAYER_MAX_DY and p.z - cam.cam.pos.z > 0:
                    px = cam.cam.pos.x
                    py = cam.cam.pos.y
                    if px > p.x and px < p.x + vars.PLANE_WIDTH and py > p.y and py < p.y + vars.PLANE_WIDTH:
                        self.pdz = -vars.PLAYER_JUMP
                        self.planeIndexTriger = index
                index = index + 1
        # Обновление рекорда
        if cam.cam.pos.z < self.record: self.record = cam.cam.pos.z
                

    def display(self):
        self.surface.fill((0, 0, 0))
        self.space.display(self.surface)
        self.planes.display(self.surface)
        pygame.display.update()

    def deinit(self):
        self.isRunning = False

    def whileWork(self):
        while self.isRunning:
            if self.timer.getMilliseconds() > (1000.0 / vars.FPS_LIMIT):
                pygame.display.set_caption('PyJumper 3D | Height: ' + str(-int(cam.cam.pos.z)) + ' | Record: ' + str(-int(self.record)) + ' | FPS: ' + str(round(1000.0 / self.timer.getMilliseconds(), 1)) + ' | ms: ' + str(round(self.timer.getMilliseconds(), 1)))
                self.timer.restart()
                self.updateEvent()
                self.updateLogic()
                self.display()