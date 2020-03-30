import pygame
import sys
from random import randint
from pygame.locals import Rect

# game constants
WIDTH = 1024
HEIGHT = 576
SCREEN_RECT = Rect(0, 0, WIDTH, HEIGHT)
X_SPEED = 0
Y_SPEED = 1
DEFAULT_RADIUS = 30


class Ball(pygame.sprite.Sprite):

    def __init__(self, initial_x, initial_y, radius=DEFAULT_RADIUS,
                 speed=[0, 0], color=(0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.radius = radius
        self.rect = Rect(
            initial_x - self.radius,
            initial_y - self.radius,
            self.radius*2,
            self.radius*2
        )
        self.color = color

    def move(self):
        self.rect.move_ip(self.speed[X_SPEED], self.speed[Y_SPEED])
        self.rect.clamp(SCREEN_RECT)

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.rect.center, self.radius, 0)


class Game:

    def __init__(self, balls_quantity):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.rect = SCREEN_RECT
        self.bg_color = (255, 255, 255)
        self.balls = []
        self.balls_quantity = balls_quantity

    def run(self):
        run = True
        for _ in range(self.balls_quantity):
            x = randint(DEFAULT_RADIUS, WIDTH - DEFAULT_RADIUS)
            y = randint(DEFAULT_RADIUS, HEIGHT - DEFAULT_RADIUS)
            speed = [0, 0]
            while speed == [0, 0]:
                speed = [randint(-10, 10), randint(-10, 10)]
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            self.balls.append(Ball(x, y, speed=speed, color=color))

        clock = pygame.time.Clock()

        while run:
            # 60 FPS
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for ball in self.balls:
                ball.move()

                # In this simple example, Game itself will control
                # the bouncing of the balls
                if ball.rect.bottom >= self.rect.height and ball.speed[Y_SPEED] > 0:
                    ball.speed[Y_SPEED] *= -1
                if ball.rect.top <= 0 and ball.speed[Y_SPEED] < 0:
                    ball.speed[Y_SPEED] *= -1
                if ball.rect.right >= self.rect.width and ball.speed[X_SPEED] > 0:
                    ball.speed[X_SPEED] *= -1
                if ball.rect.left <= 0 and ball.speed[X_SPEED] < 0:
                    ball.speed[X_SPEED] *= -1

            self.draw()

        pygame.quit()

    def draw(self):
        # paint the background color
        pygame.draw.rect(self.win, self.bg_color, self.rect)

        # draw all the balls
        for ball in self.balls:
            ball.draw(self.win)

        pygame.display.update()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        balls_quantity = int(sys.argv[1])
    else:
        balls_quantity = 10
    game = Game(balls_quantity)
    game.run()
