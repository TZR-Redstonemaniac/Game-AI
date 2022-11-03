from .Snake import Snake
from .Apple import Apple
import time
import pygame
pygame.init()


class Game_Information:
    def __init__(self, score, snakeX, snakeY, appleX, appleY):
        self.score = score - 1
        self.snakeX = snakeX
        self.snakeY = snakeY
        self.appleX = appleX
        self.appleY = appleY




class Game:
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.snake = Snake()
        self.apple = Apple()

        self.score = 0
        self.window = window

        self.death = 0

        self.resetbool = False

        self.coords = {}

        for i in range(0, self.snake.snakecount):
            self.coords.update({
                "coords" + str(i + 1): {
                    "x": self.snake.x[i],
                    "y": self.snake.y[i]
                }
            })

    def _draw_score(self):
        score_text = self.SCORE_FONT.render(f"{self.score}", 1, self.WHITE)
        self.window.blit(score_text, (self.window_width / 2 - score_text.get_width()//2, 20))

    def _draw_border(self):
        pygame.draw.line(self.window, self.RED, (0, 0), (self.window_width, 0))
        pygame.draw.line(self.window, self.RED, (0, 0), (0, self.window_height))
        pygame.draw.line(self.window, self.RED, (self.window_width - 1, 0),
                         (self.window_width - 1, self.window_height - 1))
        pygame.draw.line(self.window, self.RED, (0, self.window_height - 1),
                         (self.window_width - 1, self.window_height - 1))

    def _handle_collision(self):
        for i in range(0, len(self.snake.x)):
            self.coords.update({
                "coords" + str(i + 1): {
                    "x": self.snake.x[i],
                    "y": self.snake.y[i]
                }
            })

        for i in range(0, self.snake.snakecount):
            for j in range(0, self.snake.snakecount):
                temp = 0
                try:
                    temp = self.snake.x[i]
                except:
                    return
                else:
                    try:
                        temp = self.snake.y[i]
                    except:
                        return
                    else:
                        if i != j and self.snake.x[i] == self.coords["coords" + str(j + 1)]["x"] and \
                                self.snake.y[i] == self.coords["coords" + str(j + 1)]["y"] or self.snake.x[0] < 0 or \
                                self.snake.x[0] >= self.window_width or self.snake.y[0] < 0 or \
                                self.snake.y[0] >= self.window_height:
                            time.sleep(1)

                            while len(self.snake.x) > 0:
                                self.snake.x.pop(0)
                                self.snake.y.pop(0)
                                self.snake.snakecount -= 1
                                self.draw()
                                pygame.display.flip()
                                time.sleep(0.05)

                            self.death += 1
                            self.reset()

    def _handle_apple(self):
        temp = 0
        try:
            temp = self.snake.x[0]
        except:
            return
        else:
            try:
                temp = self.snake.y[0]
            except:
                return
            else:
                if self.apple.x == self.snake.x[0] and self.apple.y == self.snake.y[0]:
                    self.apple.x = 0
                    self.apple.y = 0
                    self.snake.x.insert(len(self.snake.x), -10)
                    self.snake.y.insert(len(self.snake.y), -10)
                    self.snake.snakecount += 1

    def draw(self):
        self.window.fill(self.BLACK)

        self._draw_score()
        self._draw_border()
        self.snake.draw(self.window)
        self.apple.draw(self.window)

    def MoveSnake(self, direction):
        self.snake.move(direction, self.coords, self.window_width, self.window_height)

    def loop(self):
        self._handle_collision()
        self._handle_apple()
        if self.apple.x == 0 or self.apple.y == 0:
            self.apple.reset()

        self.score = self.snake.snakecount - 1

        game_info = Game_Information(self.score, self.snake.x, self.snake.y, self.apple.x, self.apple.y)

        return game_info

    def reset(self):
        self.snake.reset()
        self.apple.reset()
        self.score = 0
        self.resetbool = True
