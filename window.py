import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT
from pygame.locals import *

pygame.init()

# create the game window
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Endless Runner')