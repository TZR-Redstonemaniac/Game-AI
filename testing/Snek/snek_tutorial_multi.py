from SnekGame import Game

import pygame

import neat

import os
import multiprocessing

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

            output = net.activate((self.snake.x[0], self.snake.y[0],
                                   abs(self.snake.x[0] - self.apple.x), abs(self.snake.y[0] - self.apple.y),
                                   self.snake.front, self.snake.left, self.snake.right))

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
                elif self.rightLastPress:
                    self.game.MoveSnake("up")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = True
                    self.downLastPress = False

                elif self.upLastPress:
                    self.game.MoveSnake("left")
                    self.rightLastPress = False
                    self.leftLastPress = True
                    self.upLastPress = False
                    self.downLastPress = False

                elif self.downLastPress:
                    self.game.MoveSnake("right")
                    self.rightLastPress = True
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = False


            elif decision == 1:
                if self.leftLastPress:
                    self.game.MoveSnake("left")
                    self.rightLastPress = False
                    self.leftLastPress = True
                    self.upLastPress = False
                    self.downLastPress = False

                elif self.rightLastPress:
                    self.game.MoveSnake("right")
                    self.rightLastPress = True
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = False

                elif self.upLastPress:
                    self.game.MoveSnake("up")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = True
                    self.downLastPress = False

                elif self.downLastPress:
                    self.game.MoveSnake("down")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = True

            elif decision == 2:
                if self.leftLastPress:
                    self.game.MoveSnake("up")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = True
                    self.downLastPress = False

                elif self.rightLastPress:
                    self.game.MoveSnake("down")
                    self.rightLastPress = False
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = True

                elif self.upLastPress:
                    self.game.MoveSnake("right")
                    self.rightLastPress = True
                    self.leftLastPress = False
                    self.upLastPress = False
                    self.downLastPress = False

                elif self.downLastPress:
                    self.game.MoveSnake("left")
                    self.rightLastPress = False
                    self.leftLastPress = True
                    self.upLastPress = False
                    self.downLastPress = False

            game_info = self.game.loop()

            self.game.draw()
            pygame.display.update()

            if abs(self.snake.x[0] - self.apple.x) < tempx or abs(self.snake.y[0] - self.apple.y) < tempy:
                self.calculate_fitness(genome, game_info, True, False)
                tempx = abs(self.snake.x[0] - self.apple.x)
                tempy = abs(self.snake.y[0] - self.apple.y)
            elif abs(self.snake.x[0] - self.apple.x) > tempx or abs(self.snake.y[0] - self.apple.y) > tempy:
                self.calculate_fitness(genome, game_info, False, False)
                tempx = abs(self.snake.x[0] - self.apple.x)
                tempy = abs(self.snake.y[0] - self.apple.y)
            elif self.game.score >= 1:
                self.calculate_fitness(genome, game_info, True, True)
                print("next")
                break

    def calculate_fitness(self, genome, game_info, add, done):
        if done:
            genome.fitness += game_info.score * 1000
            genome.fitness -= self.game.death * 100
        if add:
            genome.fitness += abs(self.snake.x[0] - self.apple.x)
            genome.fitness += abs(self.snake.y[0] - self.apple.y)
        else:
            genome.fitness -= abs(self.snake.x[0] - self.apple.x)
            genome.fitness -= abs(self.snake.y[0] - self.apple.y)



def eval_genome(genome, config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

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

    pe = neat.ParallelEvaluator(multiprocessing.cpu_count(), eval_genome)

    winner = p.run(pe.evaluate, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
