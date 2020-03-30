import pygame
import math
import random
from copy import deepcopy
from pygame.locals import Rect
from random import randint

# game constants
WIDTH = 1024
HEIGHT = 576
SCREEN_RECT = Rect(0, 0, WIDTH, HEIGHT)


class Wave:
    def __init__(self, center_point, bar_width=3, bar_height=20, amplitude=10, speed=5, frequency=1):
        self.center_point = center_point
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.amplitude = amplitude
        self.speed = speed
        self.frequency = frequency
        self.moved = 0
        self.bars = []
        self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        self.color_jumps = [randint(1, 10), randint(1, 10), randint(1, 10)]
        self.color_directions = [random.choice([True, False]),
                                 random.choice([True, False]),
                                 random.choice([True, False])]
        self.initialize_bars()

    def initialize_bars(self):
        self.bars = []
        self.moved = randint(0, 180)  # start at a random point
        for i in range(0, WIDTH, self.bar_width):
            self.bars.append(
                Rect(i, self.center_point, self.bar_width, self.bar_height)
            )

    def move(self):
        for index, bar in enumerate(self.bars):
            y_position = math.sin(math.radians((index+self.moved)*self.frequency))*self.amplitude
            bar.top = self.center_point - int(self.bar_height/2) + y_position
        self.moved += self.speed

    def draw(self, win):
        for bar in self.bars:
            pygame.draw.rect(win, self.color, bar)
        self.next_color()

    def next_color(self):
        for i in range(len(self.color)):
            if self.color_directions[i]:
                self.color[i] += (self.color_jumps[i]/5)
                if self.color[i] >= 256:
                    self.color[i] = 255
                    self.color_directions[i] = not self.color_directions[i]
            else:
                self.color[i] -= (self.color_jumps[i]/5)
                if self.color[i] < 0:
                    self.color[i] = 0
                    self.color_directions[i] = not self.color_directions[i]


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.rect = SCREEN_RECT
        self.bg_color = (255, 255, 255)
        self.waves = []

    def run(self):
        run = True
        self.waves = [
            Wave(
                randint(100, 200), amplitude=randint(5, 30),
                speed=randint(2, 6), bar_width=randint(2, 8),
                bar_height=randint(10, 100), frequency=randint(1, 16)/4
            ),
            Wave(
                randint(250, 350), amplitude=randint(5, 30),
                speed=randint(2, 6), bar_width=randint(2, 8),
                bar_height=randint(10, 100), frequency=randint(1, 16)/4

            ),
            Wave(
                randint(400, 550), amplitude=randint(5, 30),
                speed=randint(2, 6), bar_width=randint(2, 8),
                bar_height=randint(10, 100), frequency=randint(1, 16)/4
            ),
        ]
        clock = pygame.time.Clock()

        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()

            for layer in self.waves:
                layer.move()
        pygame.quit()

    def draw(self):
        pygame.draw.rect(self.win, self.bg_color, self.rect)

        for wave in self.waves:
            wave.draw(self.win)

        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
