import pygame, sys
from pygame.locals import *

red = [255, 0, 0]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Slither.eat - The Snake Game')

screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.flip()

while True:
# main game loop
	for event in pygame.event.get():
		print(event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()