import pygame
import random
from .Snake import Snake


class Apple:
    def __init__(self):
        x = random.randint(0, 700)
        y = random.randint(0, 500)

        x = 20 * round(x / 20)
        y = 20 * round(y / 20)

        self.snake = Snake()

        self.x = self.original_x = x
        self.y = self.original_y = y

        self.checkPos()

    def checkPos(self):
        checkforpos = True
        while checkforpos:
            for xcoord in self.snake.x:
                while xcoord == self.x:
                    self.x = random.randint(0, 700)
                    self.x = 20 * round(self.x / 20)
                    checkforpos = True
                else:
                    checkforpos = False

            for ycoord in self.snake.x:
                while ycoord == self.y:
                    self.y = random.randint(0, 500)
                    self.y = 20 * round(self.y / 20)
                    checkforpos = True
                else:
                    checkforpos = False

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (self.x + 5, self.y + 5), 5)

    def reset(self):
        x = random.randint(0, 700)
        y = random.randint(0, 500)

        x = 20 * round(x / 20)
        y = 20 * round(y / 20)

        self.x = self.original_x = x
        self.y = self.original_y = y
