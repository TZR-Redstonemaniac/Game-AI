import pygame

pygame.init()


class Board:
    def __init__(self, window, width, height):
        self.window = window
        self.window_width = width
        self.window_height = height

        self.a1x = False
        self.a2x = False
        self.a3x = False
        self.b1x = False
        self.b2x = False
        self.b3x = False
        self.c1x = False
        self.c2x = False
        self.c3x = False

        self.a1o = False
        self.a2o = False
        self.a3o = False
        self.b1o = False
        self.b2o = False
        self.b3o = False
        self.c1o = False
        self.c2o = False
        self.c3o = False

        self.count = 0

        self.x = True
        self.o = False

    def DrawGrid(self):
        pygame.draw.line(self.window, (0, 0, 0), (0, 0), (self.window_width, 0), 5)
        pygame.draw.line(self.window, (0, 0, 0), (0, 0), (0, self.window_height), 5)
        pygame.draw.line(self.window, (0, 0, 0), (self.window_width, 0), (self.window_width, self.window_height), 5)
        pygame.draw.line(self.window, (0, 0, 0), (0, self.window_height), (self.window_width, self.window_height), 5)

        pygame.draw.line(self.window, (0, 0, 0), (self.window_width * 0.33, 0),
                         (self.window_width * 0.33, self.window_height), 3)
        pygame.draw.line(self.window, (0, 0, 0), (self.window_width * 0.66, 0),
                         (self.window_width * 0.66, self.window_height), 3)
        pygame.draw.line(self.window, (0, 0, 0), (0, self.window_height * 0.33),
                         (self.window_width, self.window_height * 0.33), 3)
        pygame.draw.line(self.window, (0, 0, 0), (0, self.window_height * 0.66),
                         (self.window_width, self.window_height * 0.66), 3)

        # region X
        if self.a1x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (0, 0), (self.window_width * 0.33, self.window_height * 0.33), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.33, 0), (0, self.window_height * 0.33), 3)

        if self.a2x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (0, self.window_height * 0.33), (self.window_width * 0.33, self.window_height * 0.66), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.33, self.window_height * 0.33), (0, self.window_height * 0.66), 3)

        if self.a3x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (0, self.window_height * 0.66), (self.window_width * 0.33, self.window_height), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.33, self.window_height * 0.66), (0, self.window_height), 3)

        if self.b1x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.33, 0), (self.window_width * 0.66, self.window_height * 0.33), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.66, 0), (self.window_width * 0.33, self.window_height * 0.33), 3)

        if self.b2x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.33, self.window_height * 0.33),
                             (self.window_width * 0.66, self.window_height * 0.66), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.66, self.window_height * 0.33),
                             (self.window_width * 0.33, self.window_height * 0.66), 3)

        if self.b3x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.33, self.window_height * 0.66),
                             (self.window_width * 0.66, self.window_height), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.66, self.window_height * 0.66),
                             (self.window_width * 0.33, self.window_height), 3)

        if self.c1x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.66, 0), (self.window_width, self.window_height * 0.33), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width, 0), (self.window_width * 0.66, self.window_height * 0.33), 3)

        if self.c2x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.66, self.window_height * 0.33),
                             (self.window_width, self.window_height * 0.66), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width, self.window_height * 0.33),
                             (self.window_width * 0.66, self.window_height * 0.66), 3)

        if self.c3x:
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width * 0.66, self.window_height * 0.66),
                             (self.window_width, self.window_height), 3)
            pygame.draw.line(self.window, (0, 0, 0),
                             (self.window_width, self.window_height * 0.66),
                             (self.window_width * 0.66, self.window_height), 3)
        # endregion

        # region O
        if self.a1o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5, self.window_height * 0.33 * 0.5),
                               self.window_width * 0.33 * 0.5, 3)

        if self.a2o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5,
                                self.window_height * 0.33 * 0.5 + (self.window_height * 0.33)),
                               self.window_width * 0.33 * 0.5, 3)

        if self.a3o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5,
                                self.window_height * 0.33 * 0.5 + (self.window_height * 0.66)),
                               self.window_width * 0.33 * 0.5, 3)

        if self.b1o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5 + (self.window_width * 0.33),
                                self.window_height * 0.33 * 0.5),
                               self.window_width * 0.33 * 0.5, 3)

        if self.b2o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5 + (self.window_width * 0.33),
                                self.window_height * 0.33 * 0.5 + (self.window_height * 0.33)),
                               self.window_width * 0.33 * 0.5, 3)

        if self.b3o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5 + (self.window_width * 0.33),
                                self.window_height * 0.33 * 0.5 + (self.window_height * 0.66)),
                               self.window_width * 0.33 * 0.5, 3)

        if self.c1o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5 + (self.window_width * 0.66),
                                self.window_height * 0.33 * 0.5),
                               self.window_width * 0.33 * 0.5, 3)

        if self.c2o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5 + (self.window_width * 0.66),
                                self.window_height * 0.33 * 0.5 + (self.window_height * 0.33)),
                               self.window_width * 0.33 * 0.5, 3)

        if self.c3o:
            pygame.draw.circle(self.window, (0, 0, 0),
                               (self.window_width * 0.33 * 0.5 + (self.window_width * 0.66),
                                self.window_height * 0.33 * 0.5 + (self.window_height * 0.66)),
                               self.window_width * 0.33 * 0.5, 3)
        # endregion

    def DrawX(self, pos):
        if pos == "A1" and not self.a1o:
            self.a1x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "A2" and not self.a2o:
            self.a2x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "A3" and not self.a3o:
            self.a3x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "B1" and not self.b1o:
            self.b1x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "B2" and not self.b2o:
            self.b2x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "B3" and not self.b3o:
            self.b3x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "C1" and not self.c1o:
            self.c1x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "C2" and not self.c2o:
            self.c2x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "C3" and not self.c3o:
            self.c3x = True
            self.x = False
            self.o = True
            self.count += 1
        else:
            print("This position is not valid")

    def DrawO(self, pos):
        if pos == "A1" and not self.a1x:
            self.a1o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "A2" and not self.a2x:
            self.a2o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "A3" and not self.a3x:
            self.a3o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "B1" and not self.b1x:
            self.b1o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "B2" and not self.b2x:
            self.b2o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "B3" and not self.b3x:
            self.b3o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "C1" and not self.c1x:
            self.c1o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "C2" and not self.c2x:
            self.c2o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

        if pos == "C3" and not self.c3x:
            self.c3o = True
            self.o = False
            self.x = True
            self.count += 1
        else:
            print("This position is not valid")

    def Reset(self):
        self.a1x = False
        self.a2x = False
        self.a3x = False
        self.b1x = False
        self.b2x = False
        self.b3x = False
        self.c1x = False
        self.c2x = False
        self.c3x = False

        self.a1o = False
        self.a2o = False
        self.a3o = False
        self.b1o = False
        self.b2o = False
        self.b3o = False
        self.c1o = False
        self.c2o = False
        self.c3o = False

        self.count = 0

        self.x = True
        self.o = False
