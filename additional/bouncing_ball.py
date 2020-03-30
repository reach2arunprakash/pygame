import pygame
from pygame.locals import Rect

# game constants
WIDTH = 1024
HEIGHT = 576
SCREEN_RECT = Rect(0, 0, WIDTH, HEIGHT)
X_SPEED = 0
Y_SPEED = 1


class Ball(pygame.sprite.Sprite):
    default_radius = 30

    def __init__(self, initial_x, initial_y, radius=default_radius,
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

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.rect.center, self.radius, 0)


class Game:

    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.rect = SCREEN_RECT
        self.bg_color = (255, 255, 255)
        self.balls = []

    def run(self):
        run = True
        # Add one ball at the center. With X_SPEED = Y_SPEED = 5
        self.balls = [
            Ball(SCREEN_RECT.center[0], SCREEN_RECT.center[1], speed=[5, 5])
        ]
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
                if ball.rect.bottom >= self.rect.height or ball.rect.top <= 0:
                    ball.speed[Y_SPEED] *= -1
                if ball.rect.right >= self.rect.width or ball.rect.left <= 0:
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
    game = Game()
    game.run()
