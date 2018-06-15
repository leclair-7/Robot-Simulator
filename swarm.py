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

FPS = 20 # frames per second setting
fpsClock = pygame.time.Clock()

width,height = 800, 800
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Swarm with Balls')

class aBox:
    '''
    A box for the swarm to find a way around
    '''
    def __init__(self):
        inc = 40
        self.x   = width/9 - inc 
        self.y   = self.x
        self.w,self.h = 250,250
    
    def render(self):
        pygame.draw.rect(DISPLAYSURF, BLACK, ( self.x, self.y, self.w, self.h) )

    def get_pos(self):
        return self.x, self.y, self.w,self.h


class Agent:
    '''
    This is going to be an agent in the swarm

    Squares - because I don't know simple collision detection with circles
        - we're into swarm algorithms, not games, bucko
    '''
    def __init__(self):
        self.xpos = random.randint(5,15)
        self.ypos = random.randint(5,15)
        
        self.velocity = 5
        self.thickness = 10
        

    def render(self):
        #print((self.xpos,self.ypos))
        pygame.draw.rect(DISPLAYSURF, RED, ( self.xpos, self.ypos, self.thickness, self.thickness) )    
        #pygame.draw.circle(DISPLAYSURF, RED, (self.xpos,self.ypos), 10 )
    
    def collides(self,maybe_xpos, maybe_ypos, toAvoid):
        ####### Collision Avoidance (because I havn't done it yet) ############
        x,y,w,h = toAvoid
        if maybe_xpos > x and maybe_xpos < x + w or maybe_xpos + self.thickness > x and maybe_xpos + self.thickness < x+w:
            if maybe_ypos > y and maybe_ypos < y + h or maybe_ypos + self.thickness > y and maybe_ypos + self.thickness < y+h:
                return True
        
        ###### Phew no collisions ############################################
        return False

    def move(self, toAvoid):

        theMove = random.randint( 0, 3 )
        
        x,y,w,h = toAvoid      

        if theMove == 0:
            if self.xpos == width-1:
                self.xpos = self.xpos
            else:
                if self.collides(self.xpos + self.velocity, self.ypos, toAvoid) == False:
                    self.xpos += self.velocity
        elif theMove == 1:
            if self.ypos == height-1:
                asdfads=9
            else:
                if self.collides(self.xpos, self.ypos + self.velocity, toAvoid) == False:
                    self.ypos += self.velocity
        elif theMove == 2:
            if self.ypos == width-1:
                self.xpos=self.xpos
            elif self.ypos == height - 1:
                self.ypos=self.ypos
            else:
                if self.collides(self.xpos + self.velocity, self.ypos + self.velocity, toAvoid) == False:
                    self.xpos += self.velocity
                    self.ypos += self.velocity        

    def get_pos(self):
        return self.ypos



'''
    cx, cy 
    These are indices of centerx and centery
    Circle x-position, and yposition
'''
things = []
for i in range(5):
    thing = Agent()
    things.append(thing)
box = aBox()

while True: # the main game loop
    
    DISPLAYSURF.fill(WHITE)   
    box.render()

    pos = box.get_pos()
    x,y,w,h = pos

    for i in things:
        i.move(pos) 
        i.render()   
    
    pygame.display.update()
    fpsClock.tick(FPS)
