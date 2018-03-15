
import pygame, sys
from pygame.locals import *
from ArtPieUtils import *
pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def quitFunc():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()


