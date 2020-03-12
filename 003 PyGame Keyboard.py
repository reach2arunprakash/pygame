import pygame, sys
from pygame.locals import *

catx = 10
caty = 10
screen = 0
	
def myquit():
    ''' Self explanatory '''
    pygame.quit()
    sys.exit(0)
  
def check_inputs(events):
    global catx,caty,screen 
    ''' Function to handle events, particularly quitting the program '''
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
                elif event.key == K_LEFT:
                    catx -= 5
                    print ("Rotate image left")
                elif event.key == K_RIGHT:
                    catx += 5
                    print ("Rotate image right")
                else:
                    print (event.key)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255, 255, 255),(catx,50,50,10))
    pygame.display.update()
    print ("Rotate image right")
  
def main():
	global screen
    # Initialize Pygame
	pygame.init()  
    # Set up screen
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 480
	window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Slither.eat - The Snake Game') # Set the window bar title
	screen = pygame.display.get_surface() # This is where images are displayed
  
	pygame.display.update()

	while True:
		check_inputs(pygame.event.get())
  
main()