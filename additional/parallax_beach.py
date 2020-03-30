import pygame
import math
from pygame.locals import Rect
from random import randint

# game constants
WIDTH = 1024
HEIGHT = 576
SCREEN_RECT = Rect(0, 0, WIDTH, HEIGHT)


class BgLayer:
    def __init__(self, center_point, variability=100, speed=5,
                 color=(0, 0, 0), bar_width=3, smooth_factor=1):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.bar_width = bar_width
        self.bars = []
        self.center_point = center_point
        self.variability = variability
        self.speed = speed
        self.moved = 0
        self.smooth_factor = smooth_factor
        self.initialize_bars()

    def get_random_y(self):
        return randint(self.center_point-self.variability,
                       self.center_point+self.variability)

    def initialize_bars(self):
        self.bars = []
        # we create the array with an offset, the idea is create a full
        # circle, so we can rotate it
        degrees = math.ceil(WIDTH/360) * 360
        random_offset = randint(0, 180)  # start at a random point
        for i in range(0, degrees, self.bar_width):
            y = math.sin(math.radians(i+random_offset)) * \
                (self.variability/self.smooth_factor) + \
                self.center_point
            r = Rect(i, y, self.bar_width, WIDTH-y)
            self.bars.append(r)

    def move(self):
        # return
        max_x = -999999
        bars_outside = []
        for index, bar in enumerate(self.bars):
            # move to the left
            bar.move_ip(-1*self.speed, 0)
            max_x = max(max_x, bar.right)
            if bar.right <= 0:
                bars_outside.append(bar)

        for index, bar in enumerate(bars_outside):
            # move the bars to the right to reappear soon
            bar.left = max_x + (index * self.bar_width)

    def draw(self, win):
        for bar in self.bars:
            pygame.draw.rect(win, self.color, bar)


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.rect = SCREEN_RECT
        self.bg_color = (135, 206, 235)
        self.sun_color = (255, 237, 0)
        self.layers = []

    def run(self):
        run = True
        # Add three layers of sea. Three layers of sand
        self.layers = [
            BgLayer(
                230, variability=20, speed=1, bar_width=3, color=(0, 196, 225), smooth_factor=8
            ),
            BgLayer(
                245, variability=20, speed=1, bar_width=3, color=(0, 176, 235), smooth_factor=8
            ),
            BgLayer(
                260, variability=20, speed=1, bar_width=3, color=(0, 196, 225), smooth_factor=8
            ),
            BgLayer(
                280, variability=40, speed=2, bar_width=4, color=(217, 144, 87), smooth_factor=5
            ),
            BgLayer(
                340, variability=50, speed=5, bar_width=4, color=(197, 124, 67), smooth_factor=4
            ),
            BgLayer(
                400, variability=60, speed=10, bar_width=4, color=(177, 114, 47), smooth_factor=3
            ),
        ]
        clock = pygame.time.Clock()

        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()

            for layer in self.layers:
                layer.move()

        pygame.quit()

    def draw(self):
        # paint the background color and the sun
        pygame.draw.rect(self.win, self.bg_color, self.rect)
        pygame.draw.circle(self.win, self.sun_color, (80, 80), 50, 0)

        # draw all the balls
        for layer in self.layers:
            layer.draw(self.win)

        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
