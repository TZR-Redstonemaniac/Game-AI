from string import ascii_lowercase as alc
from .Click import Click
from .Logic import Logic
from .Score import Score
import pygame

pygame.init()


class GameInfo:
    def __init__(self, _list, x_score, o_score):
        self.input_list = _list
        self.x_score = x_score
        self.o_score = o_score


class Game:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        self.x_score = 0
        self.o_score = 0

        self.positions = {
            "a1" : False,
            "b1" : False,
            "c1" : False,
            "a2" : False,
            "b2" : False,
            "c2" : False,
            "a3" : False,
            "b3" : False,
            "c3" : False
        }



        self.input_list = []

        for i in range(0, 9):
            self.input_list.append(False)


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

        count = -1
        for i in alc:
            if i == "d" or i == "D":
                break

            for j in range(1, 4):
                count += 1
                if self.positions[f"{i}{j}"]:
                    self.input_list[count] = True
                else:
                    self.input_list[count] = False

        if self.logic.board.count == 9:
            self.Reset()

        if self.logic.board.a1x or self.logic.board.a1o:
            self.positions["a1"] = True
        else:
            self.positions["a1"] = False

        if self.logic.board.b1x or self.logic.board.b1o:
            self.positions["b1"] = True
        else:
            self.positions["b1"] = False

        if self.logic.board.c1x or self.logic.board.c1o:
            self.positions["c1"] = True
        else:
            self.positions["c1"] = False

        if self.logic.board.a2x or self.logic.board.a2o:
            self.positions["a2"] = True
        else:
            self.positions["a2"] = False

        if self.logic.board.b2x or self.logic.board.b2o:
            self.positions["b2"] = True
        else:
            self.positions["b2"] = False

        if self.logic.board.c2x or self.logic.board.c2o:
            self.positions["c2"] = True
        else:
            self.positions["c2"] = False

        if self.logic.board.a3x or self.logic.board.a3o:
            self.positions["a3"] = True
        else:
            self.positions["a3"] = False

        if self.logic.board.b3x or self.logic.board.b3o:
            self.positions["b3"] = True
        else:
            self.positions["b3"] = False

        if self.logic.board.c3x or self.logic.board.c3o:
            self.positions["c3"] = True
        else:
            self.positions["c3"] = False

        game_info = GameInfo(self.input_list, self.x_score, self.o_score)

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
