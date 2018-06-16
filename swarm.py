'''
Swarm behavior is made of simple blocks e.g. termites, ants, me as a cashier (back when..)

1 collision avoidance
2 maintaining velocity of neighbors
3 staying in proximity of neighbors

With that in mind, lets see it in pygame
'''

import pygame, sys
from pygame.locals import *
import numpy as np
import random
from math import sqrt

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

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
        self.xpos = random.randint(5,45)
        self.ypos = random.randint(5,45)
        
        self.velocity = 5
        self.thickness = 10
        self.center = sqrt((self.xpos + self.thickness/2)**2 + (self.ypos + self.thickness)**2)

    def render(self):
        pygame.draw.rect(DISPLAYSURF, RED, ( self.xpos, self.ypos, self.thickness, self.thickness) )    
        
    
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
        self.center = sqrt((self.xpos + self.thickness/2)**2 + (self.ypos + self.thickness)**2)

    def get_pos(self):
        return (self.xpos, self.ypos)


class Squirrel:

    def __init__(self,name):
        self.x=random.randint(10,25)
        self.y=random.randint(10,25)
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()

    def render(self):
        DISPLAYSURF.blit(self.image, (self.x,self.y))

# Define the bullet class to create bullets          
class Dude:

    def __init__(self,x,y,name):
        self.x = x + 23
        self.y = y
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def render(self):
        DISPLAYSURF.blit(self.image, (self.x, self.y))
    def move(self,x,y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        #self.rect = self.bullet.get_rect()
'''
    cx, cy 
    These are indices of centerx and centery
    Circle x-position, and yposition
'''
s = Squirrel("squirrel.png")
b = Dude(450,450,"boy.png")


things = []
for i in range(10):
    thing = Agent()
    things.append(thing)
box = aBox()


mousex = 450
mousey = 450

while True: # the main game loop
    
    DISPLAYSURF.fill(WHITE)   
    
    box.render()
    b.move(mousex, mousey)
    b.render()
    s.render()

    if b.is_collided_with(s):

        pos = box.get_pos()
        x,y,w,h = pos

        for i in things:
            i.move(pos) 
            i.render()   
    
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True

    pygame.display.update()
    fpsClock.tick(FPS)
