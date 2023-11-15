import time
import sys

import pygame

import gol

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_r,
    K_i,
    K_l,
    K_f,
    KEYDOWN,
    KEYUP,
    QUIT,
)


pygame.init()

WIDTH = 400
HEIGHT = 400

CELL_SIZE = 2

SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

world = gol.empty_world(WIDTH, HEIGHT)

# r-pentomino
pattern = [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]
]

gol.overwrite(world, pattern, int(WIDTH/2), int(HEIGHT/2))

old_world = gol.inverse_world(world, WIDTH, HEIGHT)

new_world = True
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            cell = world[y][x]
            old_cell = old_world[y][x]

            color = (255, 255, 255)
            if new_world:
                color = (255, 170, 170)
            if cell == 1:
                if new_world:
                    color = (0, 180, 0)
                else:
                    color = (0, 0, 0)

            if cell != old_cell:
                pygame.draw.rect(screen, color, pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    old_world = world
    world = gol.next_gol(world)
    new_world = False

    #time.sleep(.1)
