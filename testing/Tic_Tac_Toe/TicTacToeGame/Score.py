import pygame

Font = pygame.font.SysFont("comicsans", 50)


class Score:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height + 200

    def DrawScore(self, x_score, o_score):
        global Font

        self.window.fill((255, 255, 255))

        x = Font.render(f"X: {x_score}", 1, (0, 0, 0))
        o = Font.render(f"O: {o_score}", 1, (0, 0, 0))

        self.window.blit(x, (125 - x.get_width() * 0.5, self.window_height - 150))
        self.window.blit(o, (125 - x.get_width() * 0.5 + (self.window_width * 0.5), self.window_height - 150))
