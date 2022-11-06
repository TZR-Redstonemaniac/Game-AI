import pygame
from .Board import Board


class Logic:
    def __init__(self, window, window_height, window_width):
        self.window = window
        self.window_height = window_height
        self.window_width = window_width

        self.board = Board(self.window, self.window_width, self.window_height)

    def Check(self):
        # region X checks
        if self.board.a1x and self.board.a2x and self.board.a3x:
            return "x"

        if self.board.b1x and self.board.b2x and self.board.b3x:
            return "x"

        if self.board.c1x and self.board.c2x and self.board.c3x:
            return "x"

        if self.board.a1x and self.board.b1x and self.board.c1x:
            return "x"

        if self.board.a2x and self.board.b2x and self.board.c2x:
            return "x"

        if self.board.a3x and self.board.b3x and self.board.c3x:
            return "x"

        if self.board.a1x and self.board.b2x and self.board.c3x:
            return "x"

        if self.board.c1x and self.board.b2x and self.board.a3x:
            return "x"
        # endregion

        # region O checks
        if self.board.a1o and self.board.a2o and self.board.a3o:
            return "o"

        if self.board.b1o and self.board.b2o and self.board.b3o:
            return "o"

        if self.board.c1o and self.board.c2o and self.board.c3o:
            return "o"

        if self.board.a1o and self.board.b1o and self.board.c1o:
            return "o"

        if self.board.a2o and self.board.b2o and self.board.c2o:
            return "o"

        if self.board.a3o and self.board.b3o and self.board.c3o:
            return "o"

        if self.board.a1o and self.board.b2o and self.board.c3o:
            return "o"

        if self.board.c1o and self.board.b2o and self.board.a3o:
            return "o"
        # endregion

