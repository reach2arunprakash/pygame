import pygame, sys, os
from pygame.locals import * #load constants

red = [255, 0, 0]

# Initialize Pygame
pygame.init()
  
# Set up window
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Slither.eat - The Snake Game')

# Set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

count = 0

while True:
    pass
print ("Slither.eat - The Snake Game!")