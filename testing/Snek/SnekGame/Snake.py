import pygame
import time


class Snake:

    def __init__(self):
        self.snakecount = 1

        self.x = [240]
        self.y = [200]

        self.coords = {}

        self.front = False
        self.left = False
        self.right = False

    def draw(self, win):
        for i in range(0, self.snakecount):
            if i == 0:
                pygame.draw.rect(win, (30, 100, 15), (self.x[i], self.y[i], 10, 10))
            else:
                pygame.draw.rect(win, (0, 255, 0), (self.x[i], self.y[i], 10, 10))

    def move(self, dir, coords, width, height):
        match dir:
            case "up":
                if self.snakecount >= 2:
                    self.x.insert(1, self.x[0])
                    self.x.pop()

                    self.y.insert(1, self.y[0])
                    self.y.pop()

                self.y[0] -= 20

            case "down":
                if self.snakecount >= 2:
                    self.x.insert(1, self.x[0])
                    self.x.pop()

                    self.y.insert(1, self.y[0])
                    self.y.pop()

                self.y[0] += 20

            case "right":
                if self.snakecount >= 2:
                    self.x.insert(1, self.x[0])
                    self.x.pop()

                    self.y.insert(1, self.y[0])
                    self.y.pop()

                self.x[0] += 20

            case "left":
                if self.snakecount >= 2:
                    self.x.insert(1, self.x[0])
                    self.x.pop()

                    self.y.insert(1, self.y[0])
                    self.y.pop()

                self.x[0] -= 20

    def reset(self):
        self.snakecount = 1
        self.x = [240]
        self.y = [200]
        self.right = False
        self.left = False
        self.front = False
