from .Board import Board
from .Click import Click
import pygame
pygame.init()


class Game:
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        self.board = Board(self.window, self.window_width, self.window_height)
        self.click = Click(self.window_width, self.window_height)

    def GameLoop(self):
        self.board.DrawGrid()

    def CheckClick(self, pos):
        match self.click.Check(pos):
            case "A1":
                if self.board.x:
                    self.board.DrawX("A1")
                elif self.board.o:
                    self.board.DrawO("A1")

            case "B1":
                if self.board.x:
                    self.board.DrawX("B1")
                elif self.board.o:
                    self.board.DrawO("B1")

            case "C1":
                if self.board.x:
                    self.board.DrawX("C1")
                elif self.board.o:
                    self.board.DrawO("C1")

            case "A2":
                if self.board.x:
                    self.board.DrawX("A2")
                elif self.board.o:
                    self.board.DrawO("A2")

            case "B2":
                if self.board.x:
                    self.board.DrawX("B2")
                elif self.board.o:
                    self.board.DrawO("B2")

            case "C2":
                if self.board.x:
                    self.board.DrawX("C2")
                elif self.board.o:
                    self.board.DrawO("C2")

            case "A3":
                if self.board.x:
                    self.board.DrawX("A3")
                elif self.board.o:
                    self.board.DrawO("A3")

            case "B3":
                if self.board.x:
                    self.board.DrawX("B3")
                elif self.board.o:
                    self.board.DrawO("B3")

            case "C3":
                if self.board.x:
                    self.board.DrawX("C3")
                elif self.board.o:
                    self.board.DrawO("C3")
