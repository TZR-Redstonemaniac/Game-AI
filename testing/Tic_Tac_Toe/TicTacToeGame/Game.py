from .Click import Click
from .Logic import Logic
from .Score import Score
import pygame

pygame.init()


class GameInfo:
    def __init__(self, a1, a2, a3, b1, b2, b3, c1, c2, c3, x_score, o_score):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.x_score = x_score
        self.o_score = o_score


class Game:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        self.x_score = 0
        self.o_score = 0

        self.a1 = 0
        self.b1 = 0
        self.c1 = 0
        self.a2 = 0
        self.b2 = 0
        self.c2 = 0
        self.a3 = 0
        self.b3 = 0
        self.c3 = 0

        self.logic = Logic(self.window, self.window_height, self.window_width)
        self.click = Click(self.window_width, self.window_height)
        self.score = Score(self.window, self.window_width, self.window_height)

    def GameLoop(self):
        self.score.DrawScore(self.x_score, self.o_score)
        self.logic.board.DrawGrid()

        pygame.display.update()
        pygame.display.flip()

        match self.logic.Check():
            case "x":
                print("X wins!")
                self.x_score += 1
                self.Reset()
            case "o":
                print("O wins!")
                self.o_score += 1
                self.Reset()

        if self.logic.board.count == 9:
            self.Reset()

        if self.logic.board.a1x or self.logic.board.a1o:
            self.a1 = 1
        else:
            self.a1 = 0

        if self.logic.board.b1x or self.logic.board.b1o:
            self.b1 = 1
        else:
            self.b1 = 0

        if self.logic.board.c1x or self.logic.board.c1o:
            self.c1 = 1
        else:
            self.c1 = 0

        if self.logic.board.a2x or self.logic.board.a2o:
            self.a2 = 1
        else:
            self.a2 = 0

        if self.logic.board.c2x or self.logic.board.b2o:
            self.b2 = 1
        else:
            self.c2 = 0

        if self.logic.board.c2x or self.logic.board.c2o:
            self.c2 = 1
        else:
            self.c2 = 0

        if self.logic.board.a3x or self.logic.board.a3o:
            self.a3 = 1
        else:
            self.a3 = 0

        if self.logic.board.b3x or self.logic.board.b3o:
            self.b3 = 1
        else:
            self.b3 = 0

        if self.logic.board.c3x or self.logic.board.c3o:
            self.c3 = 1
        else:
            self.c3 = 0

        game_info = GameInfo(self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3,
                             self.x_score, self.o_score)

        return game_info

    def Reset(self):
        self.logic.board.Reset()

    def TotalReset(self):
        self.x_score = 0
        self.o_score = 0
        self.logic.board.Reset()

    def CheckClick(self, pos, override):
        match self.click.Check(pos, override):
            case "A1":
                if self.logic.board.x:
                    self.logic.board.DrawX("A1")
                elif self.logic.board.o:
                    self.logic.board.DrawO("A1")

            case "B1":
                if self.logic.board.x:
                    self.logic.board.DrawX("B1")
                elif self.logic.board.o:
                    self.logic.board.DrawO("B1")

            case "C1":
                if self.logic.board.x:
                    self.logic.board.DrawX("C1")
                elif self.logic.board.o:
                    self.logic.board.DrawO("C1")

            case "A2":
                if self.logic.board.x:
                    self.logic.board.DrawX("A2")
                elif self.logic.board.o:
                    self.logic.board.DrawO("A2")

            case "B2":
                if self.logic.board.x:
                    self.logic.board.DrawX("B2")
                elif self.logic.board.o:
                    self.logic.board.DrawO("B2")

            case "C2":
                if self.logic.board.x:
                    self.logic.board.DrawX("C2")
                elif self.logic.board.o:
                    self.logic.board.DrawO("C2")

            case "A3":
                if self.logic.board.x:
                    self.logic.board.DrawX("A3")
                elif self.logic.board.o:
                    self.logic.board.DrawO("A3")

            case "B3":
                if self.logic.board.x:
                    self.logic.board.DrawX("B3")
                elif self.logic.board.o:
                    self.logic.board.DrawO("B3")

            case "C3":
                if self.logic.board.x:
                    self.logic.board.DrawX("C3")
                elif self.logic.board.o:
                    self.logic.board.DrawO("C3")
