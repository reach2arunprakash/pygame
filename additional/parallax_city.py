import pygame
from pygame.locals import Rect
from random import randint

# game constants
WIDTH = 1024
HEIGHT = 576
SCREEN_RECT = Rect(0, 0, WIDTH, HEIGHT)


class BgLayer:
    def __init__(self, center_point, variability=100, speed=5,
                 color=(0, 0, 0), bar_width=10):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.bar_width = bar_width
        self.bars = []
        self.center_point = center_point
        self.variability = variability
        self.speed = speed
        self.initialize_bars()

    def get_random_y(self):
        return randint(self.center_point-self.variability,
                       self.center_point+self.variability)

    def initialize_bars(self):
        self.bars = []
        for i in range(0, WIDTH+self.bar_width*2, self.bar_width):
            y = self.get_random_y()
            r = Rect(i, y, self.bar_width, WIDTH-y)
            self.bars.append(r)

    def move(self, random=True):
        max_x = -999999
        bars_outside = []
        for index, bar in enumerate(self.bars):
            # move to the left
            bar.move_ip(-1*self.speed, 0)
            max_x = max(max_x, bar.right)
            if bar.right < 0:
                bars_outside.append(bar)

        for index, bar in enumerate(bars_outside):
            # move the bars to the right to reappear soon
            bar.left = max_x + (index * self.bar_width)
            if random:   # also, if random is set, recalculate the Y
                bar.top = self.get_random_y()

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
        # Add three layers.
        self.layers = [
            BgLayer(280, variability=40, speed=1, bar_width=15, color=(111, 111, 111)),
            BgLayer(340, variability=50, speed=2, bar_width=20, color=(50, 50, 50)),
            BgLayer(400, variability=60, speed=5, bar_width=30),
            # Wave(500, variability=2, speed=5, bar_width=15, color=(177, 114, 47))
        ]
        clock = pygame.time.Clock()

        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for layer in self.layers:
                layer.move()

            self.draw()

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
