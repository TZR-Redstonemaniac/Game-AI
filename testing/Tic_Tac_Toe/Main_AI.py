from TicTacToeGame import Game
import pygame
import neat
import os

pygame.display.set_caption("Tic-Tac-Toe")


class MainGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.game.CheckClick(pos, False)

            self.game.GameLoop()

            pygame.display.update()

        pygame.quit()

    def Train_AI(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output1 = net1.activate((self.game.a1, self.game.b1, self.game.c1, self.game.a2, self.game.b2, self.game.c2,
                                     self.game.a3, self.game.b3, self.game.c3, self.game.x_score, self.game.o_score))

            decision1 = output1.index(max(output1))

            match decision1:
                case 0:
                    self.game.CheckClick("A1", True)

                case 1:
                    self.game.CheckClick("B1", True)

                case 2:
                    self.game.CheckClick("C1", True)

                case 3:
                    self.game.CheckClick("A2", True)

                case 4:
                    self.game.CheckClick("B2", True)

                case 5:
                    self.game.CheckClick("C2", True)

                case 6:
                    self.game.CheckClick("A3", True)

                case 7:
                    self.game.CheckClick("B3", True)

                case 8:
                    self.game.CheckClick("C3", True)

            output2 = net2.activate((self.game.a1, self.game.b1, self.game.c1, self.game.a2, self.game.b2, self.game.c2,
                                     self.game.a3, self.game.b3, self.game.c3, self.game.x_score, self.game.o_score))

            decision2 = output2.index(max(output2))

            match decision2:
                case 0:
                    self.game.CheckClick("A1", True)

                case 1:
                    self.game.CheckClick("B1", True)

                case 2:
                    self.game.CheckClick("C1", True)

                case 3:
                    self.game.CheckClick("A2", True)

                case 4:
                    self.game.CheckClick("B2", True)

                case 5:
                    self.game.CheckClick("C2", True)

                case 6:
                    self.game.CheckClick("A3", True)

                case 7:
                    self.game.CheckClick("B3", True)

                case 8:
                    self.game.CheckClick("C3", True)

            print(output1, output2)

            game_info = self.game.GameLoop()
            pygame.display.update()

            if game_info.x_score >= 1 or game_info.o_score >= 1:
                self.calculate_fitness(genome1, genome2, game_info)

    def calculate_fitness(self, genome1, genome2, game_info):
        pass



def eval_genomes(genomes, config):
    width, height = 500, 700
    window = pygame.display.set_mode((width, height + 200))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break

        genome1.fitness = 0

        for genome_id2, genome2 in genomes[i + 1:]:
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness

            game = MainGame(window, width, height)

            game.Train_AI(genome1, genome2, config)


def run_neat(config):
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter())
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    p.run(eval_genomes, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "Config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)
