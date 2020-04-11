#!/usr/bin/env python3
import pygame
import time
import random

SCREEN_W, SCREEN_H, CELL_SIZE = 1280, 720, 20
COLOR, BG_COLOR = (0x39, 0x3d, 0x31), (0xa0, 0xa3, 0x8a)
snake = []
food = (0, 0)
is_gameover = False
direct_x, direct_y = 1, -1


def drawNode(win, node):
    x, y = node
    pygame.draw.rect(win, COLOR, ((int(x+1), int(y+1)),
                                  (CELL_SIZE-2, CELL_SIZE-2)))
    pygame.draw.rect(win, BG_COLOR, ((int(x+CELL_SIZE/8+1), int(y+CELL_SIZE/8+1)),
                                     (CELL_SIZE-CELL_SIZE/4-1, CELL_SIZE-CELL_SIZE/4-1)))
    pygame.draw.rect(win, COLOR, ((int(x+CELL_SIZE/4), int(y+CELL_SIZE/4)),
                                  (CELL_SIZE/2, CELL_SIZE/2)))


def reset():
    global snake, food, direct_x, direct_y, is_gameover
    snake = [(140, 300), (120, 300), (100, 300)]
    food = (randomPos(SCREEN_W), randomPos(SCREEN_H))
    direct_x, direct_y = 1, 0
    is_gameover = False


def trun(key):
    global direct_x, direct_y
    if direct_y == 0:
        if key == pygame.K_UP:
            direct_x, direct_y = 0, -1
        elif key == pygame.K_DOWN:
            direct_x, direct_y = 0, 1
    elif direct_x == 0:
        if key == pygame.K_LEFT:
            direct_x, direct_y = -1, 0
        elif key == pygame.K_RIGHT:
            direct_x, direct_y = 1, 0


def randomPos(leng):
    return int(random.random() * leng / CELL_SIZE) * CELL_SIZE


def move():
    global snake, food, direct_x, direct_y, is_gameover
    x, y = snake[0]
    if x < 0 or x >= SCREEN_W or y < 0 or y >= SCREEN_H or snake[0] in snake[1:]:
        is_gameover = True
        return
    snake.insert(0, (x+direct_x*CELL_SIZE, y+direct_y*CELL_SIZE))
    if food in snake:
        food = (randomPos(SCREEN_W), randomPos(SCREEN_H))
    else:
        snake.pop()


def draw(win):
    game_over = [
        (3, 2), (4, 2), (5, 2), (6, 2), (2, 3), (2, 4), (2, 5), (3, 6), (4, 6),
        (5, 6), (6, 6), (6, 5), (6, 4), (5, 4),  # G
        (9, 4), (9, 5), (9, 6), (10, 3), (11, 2), (12, 3), (13, 4), (13, 5),
        (13, 6), (10, 5), (11, 5), (12, 5),  # A
        (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (17, 3), (18, 4), (19, 3),
        (20, 2), (20, 3), (20, 4), (20, 5), (20, 6),  # M
        (23, 2), (24, 2), (25, 2), (26, 2), (27, 2), (23, 3), (23, 4), (23, 5),
        (23, 6), (24, 6), (25, 6), (26, 6), (27, 6), (24, 4), (25, 4),  # E
        (2, 10), (2, 11), (2, 12), (3, 9), (4, 9), (5, 9), (6, 10), (6, 11),
        (6, 12), (3, 13), (4, 13), (5, 13),  # O
        (9, 9), (9, 10), (9, 11), (13, 9), (13, 10), (13, 11), (10, 12),
        (11, 13), (12, 12),  # V
        (16, 9), (17, 9), (18, 9), (19, 9), (20, 9), (16, 10), (16, 11), (16, 12),
        (16, 13), (17, 13), (18, 13), (19, 13), (20, 13), (17, 11), (18, 11),  # E
        (23, 9), (23, 10), (23, 11), (23, 12), (23, 13), (24, 9), (25, 9), (26, 9),
        (24, 11), (25, 11), (26, 11), (27, 10), (27, 12), (27, 13)]  # R
    if is_gameover:
        snake = list(map(
            lambda pos: ((pos[0]+17)*CELL_SIZE, (pos[1]+8)*CELL_SIZE), game_over))
    else:
        drawNode(win, food)

    for node in snake:
        drawNode(win, node)


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    reset()
    running = True
    while running:
        clock.tick(5)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                else:
                    reset() if is_gameover else trun(e.key)

        win.fill(BG_COLOR, (0, 0, SCREEN_W, SCREEN_H))
        move()
        draw(win)
        pygame.display.flip()
    pygame.quit()
