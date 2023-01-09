import time
import random



def next_gol(world):
    world_h = len(world)
    world_w = len(world[0])

    new_world = [[0]*world_w for _ in range(0, world_h)]

    for y in range(0, world_h):
        for x in range(0, world_w):
            is_live = world[y][x]
            live_neighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not (i == 0 and j == 0):
                        n_y = (y + i) % world_h
                        n_x = (x + j) % world_w
                        live_neighbors += world[n_y][n_x]

            if is_live:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_world[y][x] = 1
            else:
                if live_neighbors == 3:
                    new_world[y][x] = 1


    return new_world



def iterate_gol(arr):
    while True:
        new_world = next_gol(arr)
        print_world(new_world)
        arr = new_world
        time.sleep(.05)


def print_world(world):
    print(''.join(['-' for _ in range(len(world[0]))]))
    for y in range(0, len(world)):
        out_str = '|'
        for x in range(0, len(world[y])):
            if world[y][x] == 0:
                out_str += ' '
            else:
                out_str += 'X'
        out_str += '|'
        print(out_str)
    print(''.join(['-' for _ in range(len(world[0]))]))


def overwrite(world, pattern, x, y):
    for j in range(len(pattern)):
        for i in range(len(pattern[j])):
            world[y+j][x+i] = pattern[j][i]

if __name__ == '__main__':
    width = 50
    height = 25
    start_arr = [[0 for i in range(width)] for _ in range(height)]
    pattern = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
    ]
    pattern = [
            [0, 1, 1],
            [1, 1, 0],
            [0, 1, 0]
    ]

    overwrite(start_arr, pattern, int(width/2), int(height/2))
    iterate_gol(start_arr)
