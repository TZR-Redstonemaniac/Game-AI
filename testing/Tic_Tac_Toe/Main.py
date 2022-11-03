from TicTacToeGame import Game
import pygame

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
                    self.game.CheckClick(pos)

            self.game.GameLoop()

            pygame.display.update()


if __name__ == "__main__":
    width, height = 700, 900
    window = pygame.display.set_mode((width, height))

    game = MainGame(window, width, height)

    game.run()
