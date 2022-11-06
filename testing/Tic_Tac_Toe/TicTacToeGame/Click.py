import pygame


class Click:
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height

    def Check(self, pos, override):
        if not override:
            if pos[0] < self.window_width * 0.33 and pos[1] < self.window_height * 0.33:
                return "A1"

            if pos[0] < self.window_width * 0.33 and self.window_height * 0.66 > pos[1] > self.window_height * 0.33:
                return "A2"

            if pos[0] < self.window_width * 0.33 and self.window_height > pos[1] > self.window_height * 0.66:
                return "A3"

            if self.window_width * 0.66 > pos[0] > self.window_width * 0.33 and pos[1] < self.window_height * 0.33:
                return "B1"

            if self.window_width * 0.66 > pos[0] > self.window_width * 0.33 and \
                    self.window_height * 0.66 > pos[1] > self.window_height * 0.33:
                return "B2"

            if self.window_width * 0.66 > pos[0] > self.window_width * 0.33 and\
                    self.window_height > pos[1] > self.window_height * 0.66:
                return "B3"

            if pos[0] > self.window_width * 0.66 and pos[1] < self.window_height * 0.33:
                return "C1"

            if pos[0] > self.window_width * 0.66 and self.window_height * 0.66 > pos[1] > self.window_height * 0.33:
                return "C2"

            if pos[0] > self.window_width * 0.66 and self.window_height > pos[1] > self.window_height * 0.66:
                return "C3"
        elif override:
            return pos
