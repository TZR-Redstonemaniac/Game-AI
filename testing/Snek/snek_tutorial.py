import math

from SnekGame import Game

import pygame

import neat

import os

import random
import time

pygame.display.set_caption("Snek")

run = 1


class SnakeGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.snake = self.game.snake
        self.apple = self.game.apple

        self.rightLastPress = False
        self.leftLastPress = False
        self.upLastPress = False
        self.downLastPress = False

        num = random.randint(0, 3)

        if num == 0:
            self.rightLastPress = True
        elif num == 1:
            self.downLastPress = True
        elif num == 2:
            self.leftLastPress = True
        elif num == 3:
            self.upLastPress = True

        self.game.resetbool = False

    def test_ai(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and not self.downLastPress:
                game.MoveSnake("up")
                self.rightLastPress = False
                self.leftLastPress = False
                self.upLastPress = True
                self.downLastPress = False
                game.resetbool = False
            elif self.upLastPress:
                game.MoveSnake("up")

            if keys[pygame.K_LEFT] and not self.rightLastPress:
                game.MoveSnake("left")
                self.rightLastPress = False
                self.leftLastPress = True
                self.upLastPress = False
                self.downLastPress = False
                game.resetbool = False
            elif self.leftLastPress:
                game.MoveSnake("left")

            if keys[pygame.K_DOWN] and not self.upLastPress:
                game.MoveSnake("down")
                self.rightLastPress = False
                self.leftLastPress = False
                self.upLastPress = False
                self.downLastPress = True
                game.resetbool = False
            elif self.downLastPress:
                game.MoveSnake("down")

            if keys[pygame.K_RIGHT] and not self.leftLastPress:
                game.MoveSnake("right")
                self.rightLastPress = True
                self.leftLastPress = False
                self.upLastPress = False
                self.downLastPress = False
                game.resetbool = False
            elif self.rightLastPress:
                game.MoveSnake("right")

            game_info = game.loop()
            print(game_info.score)
            game.draw()

            if game.resetbool:
                self.rightLastPress = False
                self.leftLastPress = False
                self.upLastPress = False
                self.downLastPress = False

            pygame.display.update()

        pygame.quit()

    def train_ai(self, genome, config):

        net = neat.nn.FeedForwardNetwork.create(genome, config)

        tempx = abs(self.snake.x[0] - self.apple.x)
        tempy = abs(self.snake.y[0] - self.apple.y)

        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return quit()



            output = net.activate((abs(self.snake.x[0] - self.apple.x), abs(self.snake.y[0] - self.apple.y),
                                   self.angle(self.snake.x[0] - self.apple.x, self.snake.y[0] - self.apple.y)))

            decision = output.index(max(output))

            tempx = abs(self.snake.x[0] - self.apple.x)
            tempy = abs(self.snake.y[0] - self.apple.y)

            if decision == 0:
                if self.leftLastPress:
                    self.game.MoveSnake("down")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = True
                    self.check_surrounding("down")
                elif self.rightLastPress:
                    self.game.MoveSnake("up")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = True
                    self.downLastPress = False
                    self.check_surrounding("up")

                elif self.upLastPress:
                    self.game.MoveSnake("left")
                    self.rightLastPress = False
                    self.leftLastPress = True
                    self.upLastPress = False
                    self.downLastPress = False
                    self.check_surrounding("left")

                elif self.downLastPress:
                    self.game.MoveSnake("right")
                    self.rightLastPress = True
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = False
                    self.check_surrounding("right")


            elif decision == 1:
                if self.leftLastPress:
                    self.game.MoveSnake("left")
                    self.rightLastPress = False
                    self.leftLastPress = True
                    self.upLastPress = False
                    self.downLastPress = False
                    self.check_surrounding("left")

                elif self.rightLastPress:
                    self.game.MoveSnake("right")
                    self.rightLastPress = True
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = False
                    self.check_surrounding("right")

                elif self.upLastPress:
                    self.game.MoveSnake("up")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = True
                    self.downLastPress = False
                    self.check_surrounding("up")

                elif self.downLastPress:
                    self.game.MoveSnake("down")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = True
                    self.check_surrounding("down")

            elif decision == 2:
                if self.leftLastPress:
                    self.game.MoveSnake("up")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = True
                    self.downLastPress = False
                    self.check_surrounding("up")

                elif self.rightLastPress:
                    self.game.MoveSnake("down")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = True
                    self.check_surrounding("down")

                elif self.upLastPress:
                    self.game.MoveSnake("right")
                    self.rightLastPress = True
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = False
                    self.check_surrounding("right")

                elif self.downLastPress:
                    self.game.MoveSnake("left")
                    self.rightLastPress = False
                    self.leftLastPress = True
                    self.upLastPress = False
                    self.downLastPress = False
                    self.check_surrounding("left")

            game_info = self.game.loop()

            self.game.draw()
            pygame.display.update()


            if self.game.score >= 1:
                self.calculate_fitness(genome, game_info)
                print("next")
                break

    def calculate_fitness(self, genome, game_info):
        genome.fitness += game_info.score * 1000
        genome.fitness -= self.game.death * 100

    def angle(self, xdistance, ydistance):
        x = ""
        y = ""

        angle = 0

        if xdistance < 0:
            x = "+"
        else:
            x = "-"

        if ydistance < 0:
            y = "+"
        else:
            y = "-"

        xd = abs(xdistance)
        yd = abs(ydistance)

        if y == "+" and x == "+":
            angle = math.degrees(math.atan(yd/xd)) + 90

        if y == "-" and x == "+":
            angle = 90 - math.degrees(math.atan(yd/xd))

        if y == "+" and x == "-":
            angle = math.degrees(math.atan(yd/xd)) + 180

        if y == "-" and x == "-":
            angle = math.degrees(math.atan(yd/xd)) + 270

        return round(angle, 2)


    def check_surrounding(self, dir):
        match dir:
            case "right":
                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] + 20 == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.front = True
                    elif self.snake.x[0] + 20 >= self.game.window_width:
                        self.snake.front = True
                    else:
                        self.snake.front = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] - 20 == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.left = True
                    elif self.snake.y[0] - 20 < 0:
                        self.snake.left = True
                    else:
                        self.snake.left = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] + 20 == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.right = True
                    elif self.snake.y[0] + 20 >= self.game.window_height:
                        self.snake.right = True
                    else:
                        self.snake.right = False

            case "left":
                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] - 20 == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.front = True
                    elif self.snake.x[0] - 20 < 0:
                        self.snake.front = True
                    else:
                        self.snake.front = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] + 20 == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.left = True
                    elif self.snake.y[0] + 20 >= self.game.window_height:
                        self.snake.left = True
                    else:
                        self.snake.left = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] - 20 == self.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.right = True
                    elif self.snake.y[0] - 20 >= self.game.window_height:
                        self.snake.right = True
                    else:
                        self.snake.right = False

            case "up":
                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] - 20 == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.front = True
                    elif self.snake.y[0] - 20 < 0:
                        self.snake.front = True
                    else:
                        self.snake.front = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] - 20 == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.left = True
                    elif self.snake.x[0] - 20 < 0:
                        self.snake.left = True
                    else:
                        self.snake.left = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] + 20 == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.right = True
                    elif self.snake.x[0] + 20 >= self.game.window_width:
                        self.snake.right = True
                    else:
                        self.snake.right = False

            case "down":
                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] + 20 == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.front = True
                    elif self.snake.y[0] + 20 >= self.game.window_height:
                        self.snake.front = True
                    else:
                        self.snake.front = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] + 20 == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.y[0] == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.left = True
                    elif self.snake.x[0] + 20 >= self.game.window_width:
                        self.snake.left = True
                    else:
                        self.snake.left = False

                for j in range(0, self.snake.snakecount):
                    if self.snake.x[0] - 20 == self.game.coords.get("coords" + str(j + 1)).get("x") and \
                            self.snake.y[0] == self.game.coords.get("coords" + str(j + 1)).get("y"):
                        self.snake.right = True
                    elif self.snake.x[0] - 20 < 0:
                        self.snake.right = True
                    else:
                        self.snake.right = False


def eval_genomes(genomes, config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0 if genome.fitness is None else genome.fitness
        game = SnakeGame(window, width, height)
        game.train_ai(genome, config)


def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint("")
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter())
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
