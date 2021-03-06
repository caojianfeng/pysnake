#!/usr/bin/env python3
# author: caojianfeng(windcao@hotmail.com)
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
    global snake, food, is_gameover
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
    if is_gameover:
        game_over = pygame.font.Font(None, 60).render("GAME OVER", True, COLOR)
        game_over_rect = game_over.get_rect()
        game_over_rect.center = (SCREEN_W/2, SCREEN_H/2)
        win.blit(game_over, game_over_rect)

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
