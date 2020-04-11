import pygame


class Snake(object):

    def __init__(self):
        self.x = 100
        self.y = 200
        self.speed = 1
        self.dirction_x = 1
        self.dirction_y = 0

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 100), (self.x, self.y), 10)
        self.x += self.speed*self.dirction_x
        self.y += self.speed*self.dirction_y

    def move(self, key):
        if key == pygame.K_DOWN and self.dirction_y == 0:
            self.dirction_x = 0
            self.dirction_y = 1
        elif key == pygame.K_UP and self.dirction_y == 0:
            self.dirction_x = 0
            self.dirction_y = -1
        elif key == pygame.K_LEFT and self.dirction_x == 0:
            self.dirction_x = -1
            self.dirction_y = 0
        elif key == pygame.K_RIGHT and self.dirction_x == 0:
            self.dirction_x = 1
            self.dirction_y = 0
