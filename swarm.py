'''
Swarm behavior is made of simple blocks e.g. termites, ants, me as a cashier (back when..)

1 collision avoidance
2 maintaining velocity of neighbors
3 staying in proximity of neighbors

With that in mind, lets see it in pygame
'''

import pygame, sys
from pygame.locals import *
pygame.init()
from ArtPieUtils import *
from A_star import search
from pprint import pprint
import numpy as np
import random

FPS = 8 # frames per second setting
fpsClock = pygame.time.Clock()

width,height = 500, 500
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Swarm with Balls')

#def putTextOnScreen(s="Hi, Lucas",position = (200,150)):
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObject = fontObj.render ("Hi Swarm", True, GREEN, BLUE)
textRectObj = textSurfaceObject.get_rect()
textRectObj.center = (200,150)

class Agent:
    '''
    This is going to be an agent in the swarm

    width // gridSize
    '''
    def __init__(self):
        self.xpos = random.randint(10,25)
        self.ypos = random.randint(10,25)

        self.centerx = []
        self.centery = []
        
        self.cx = 0
        self.cy = 0

        increment = width // gridSize

        prevCoordx = 4
        for i in range(0,width , increment):   
            self.centerx.append((prevCoordx + increment//2 ) )
            prevCoordx += increment
        prevCoordy = 4
        for i in range(0,height, increment):
            self.centery.append(prevCoordy + (increment)//2 )
            prevCoordy += increment

    def showThis(self):    
        pygame.draw.circle(DISPLAYSURF, RED, (self.xpos,self.ypos), width // gridSize // 3 )
    def move(self):
        theMove = random.randint( 0, 3 )

        if theMove == 0:
            if self.cx == len(self.centerx)-1:
                self.cx = 0
            else:
                self.cx += 1
        elif theMove == 1:
            if self.cy == len(self.centery)-1:
                asdfads=9
            else:
                self.cy += 1
        elif theMove == 2:
            if self.cx == len(self.centerx)-1:
                self.cx=0
            elif self.cy == len(self.centery)-1:
                self.cy=0
            else:
                self.cx += 1
                self.cy += 1
        else:
            pass
        self.xpos = self.centerx[self.cx]
        self.ypos = self.centery[self.cy]

    def get_pos(self):
        return self.cy

gridSize = 25

'''
    cx, cy 
    These are indices of centerx and centery
    Circle x-position, and yposition
'''
things = []
for i in range(5):
    thing = Agent()
    things.append(thing)

while True: # the main game loop
    
    DISPLAYSURF.fill(WHITE)   
    
    for i in things:
        i.move() 
        i.showThis()   
    
    pygame.display.update()
    fpsClock.tick(FPS)


def humanControls():
    for event in pygame.event.get():
        if event.type == QUIT:
            quitFunc()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:
                quitFunc()

            elif event.key == pygame.K_UP:
                if cy == 0:
                    pass
                else:
                    cy -= 1

            elif event.key == pygame.K_DOWN:
                if cy == len(centery)-1:
                    pass
                else:
                    cy += 1

            elif event.key == pygame.K_LEFT:
                if cx == 0:
                    pass
                else:
                    cx -= 1

            elif event.key == pygame.K_RIGHT:
                if cx == len(centerx)-1:
                    pass
                else:
                    cx += 1