import random

import pygame as pg

wsize = (720, 480)          #turple

screen = pg.display.set_mode(wsize)

tsize = 30
msize = wsize[0] // tsize, wsize[1] // tsize

stapt_pos = wsize[0] // 2, wsize[1] // 2

snale = [stapt_pos]
alive = True

direction = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

apple = random.randint(0, msize[0]), random.randint(0, msize[1])

running = True
while running:
    screen.fill("black")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    [pg.draw.rect(screen, 'green', (x * tsize, y * tsize, tsize - 1, tsize - 1)) for x, y in snake]
    pg.draw.rect(screen, 'red', (apple[0] * tsize, apple[1] * tsize, tsize - 1, tsize - 1))

    if alive:
        new_pos = snake[0][0] + directions[direction    ]
