import engine

engine = engine.Engine()
engine.init()
engine.whileWork()
engine.deinit()
quit()

# import pygame
# import random
# from timer import Timer

# DISPLAY_WIDTH = 1000
# DISPLAY_HEIGHT = 1000
# NUM_CELLS_X = 20
# NUM_CELLS_Y = 20
# SPEED_START = 1000.0
# SPEED_DOWN_PER = 0.15 # SPEED_START - SPEED_START * SPEED_DOWN_PER

# pygame.init()
# display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# pygame.display.update()
# pygame.display.set_caption('Какой то тест Python')

# isRunning = True

# fd_posX = random.randint(0, NUM_CELLS_X - 1)
# fd_posY = random.randint(0, NUM_CELLS_Y - 1)

# sn_posX = 0
# sn_posY = 0
# sn_dir = 1
# sn_speed = SPEED_START

# t_event = Timer() 
# t_render = Timer() 

# while isRunning:
#     # События
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: isRunning = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:         
#                 if sn_dir == 0: 
#                     sn_posY = sn_posY - 1 
#                     t_event.restart()
#                 else: 
#                     sn_dir = 0
#             elif event.key == pygame.K_RIGHT:    
#                 if sn_dir == 1: 
#                     sn_posX = sn_posX + 1 
#                     t_event.restart()
#                 else: 
#                     sn_dir = 1
#             elif event.key == pygame.K_DOWN:     
#                 if sn_dir == 2: 
#                     sn_posY = sn_posY + 1 
#                     t_event.restart()
#                 else: 
#                     sn_dir = 2
#             elif event.key == pygame.K_LEFT:
#                 if sn_dir == 3: 
#                     sn_posX = sn_posX - 1 
#                     t_event.restart()
#                 else: 
#                     sn_dir = 3

#     if t_event.getMilliseconds() > sn_speed:
#         t_event.restart()

#         if sn_dir == 0: sn_posY = sn_posY - 1
#         elif sn_dir == 1: sn_posX = sn_posX + 1
#         elif sn_dir == 2: sn_posY = sn_posY + 1
#         elif sn_dir == 3: sn_posX = sn_posX - 1

#     if sn_posX > NUM_CELLS_X - 1: sn_posX = 0
#     elif sn_posX < 0: sn_posX = NUM_CELLS_X - 1
#     if sn_posY > NUM_CELLS_Y - 1: sn_posY = 0
#     elif sn_posY < 0: sn_posY = NUM_CELLS_Y - 1

#     if sn_posX == fd_posX and sn_posY == fd_posY:
#         fd_posX = random.randint(0, NUM_CELLS_X - 1)
#         fd_posY = random.randint(0, NUM_CELLS_Y - 1)
#         sn_speed = sn_speed - (sn_speed * SPEED_DOWN_PER)

#     if t_render.getMilliseconds() > 1000.0 / 60.0:
#         t_render.restart()
#         # Чистка экрана
#         display.fill((0, 0, 0, 1))

#         # Вывод объектов
#         pygame.draw.rect(display, (200, 200, 200), pygame.Rect(
#             (DISPLAY_WIDTH / NUM_CELLS_X) * (sn_posX),
#             (DISPLAY_HEIGHT / NUM_CELLS_Y) * (sn_posY),
#             (DISPLAY_WIDTH / NUM_CELLS_X),
#             (DISPLAY_HEIGHT / NUM_CELLS_Y),
#             ))

#         pygame.draw.rect(display, (255, 0, 0), pygame.Rect(
#             (DISPLAY_WIDTH / NUM_CELLS_X) * (fd_posX),
#             (DISPLAY_HEIGHT / NUM_CELLS_Y) * (fd_posY),
#             (DISPLAY_WIDTH / NUM_CELLS_X),
#             (DISPLAY_HEIGHT / NUM_CELLS_Y),
#             ))

#         # Вывод сетки
#         for x in range(1, NUM_CELLS_X):
#             pygame.draw.line(display, (60, 60, 60), [(DISPLAY_WIDTH / NUM_CELLS_X) * x, 0], [(DISPLAY_WIDTH / NUM_CELLS_X) * x, DISPLAY_HEIGHT])
#         for y in range(1, NUM_CELLS_Y):
#             pygame.draw.line(display, (60, 60, 60), [0, (DISPLAY_HEIGHT / NUM_CELLS_Y) * y], [DISPLAY_WIDTH, (DISPLAY_HEIGHT / NUM_CELLS_Y) * y])


#         # Вывод и задержка
#         pygame.display.update()
        


# pygame.quit()
# quit()