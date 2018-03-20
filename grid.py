'''
Made by Lucas working through Al Swiegart's book, Making Games with Python & Pygame
'''
import pygame, sys
from pygame.locals import *
pygame.init()
from ArtPieUtils import *
from A_star import search
from pprint import pprint
import numpy as np


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#this will make the grid, 5x5
gridSize = 5

#grid line width
gridLineWidth = 4

width,height = 400, 400
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('A Star with a Red Ball')

anImg = pygame.image.load('anImg.png')

#def putTextOnScreen(s="Hi, Lucas",position = (200,150)):
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObject = fontObj.render ("Hi Lucas", True, GREEN, BLUE)
textRectObj = textSurfaceObject.get_rect()
textRectObj.center = (200,150)

def drawCircle(x,y):
    #circle(Surface, color, pos, radius, width=0) 0 width means it'll filled
    pygame.draw.circle(DISPLAYSURF, RED, (x,y), width // gridSize // 3 )


####### Gets coordinates of circle centers ####### 
centerx = []
centery = []
increment = width // gridSize

prevCoordx = 4
for i in range(0,width , increment):   
    centerx.append((prevCoordx + increment//2 ) )
    prevCoordx += increment

prevCoordy = 4
for i in range(0,height, increment):
    centery.append(prevCoordy + (increment)//2 )
    prevCoordy += increment
#####################################################

h = []
for i in centerx:
    a = []
    for j in centery:
        a.append((i,j) )
    h.append(a)

grid = [[0, 1,  0, 0, 0],
            [0, 1,  0, 0, 0],
            [0, 1,  0, 0, 0],
            [0, 1,  0, 0, 0],
            [0, 0,  0, 1, 0]]

heuristic = [[9, 8, 6, 5, 4],
             [8, 7, 5, 4, 3],
             [7, 6, 4, 3, 2],
             [6, 5, 3, 2, 1],
             [5, 4, 2, 1, 0]]

goal = [4,4]
cost = 1

assert len(grid) == gridSize, "gridsize has to be the grid for the mapping to occur"

def drawGrid():
    for i in range(0,height, increment):
        #draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLUE, (i, 0), (i, height), gridLineWidth)
        #draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLUE, (0, i), (width, i), gridLineWidth)

def putWallsOn():

    for i in range(len(grid) ):
        for j in range(len( grid[0] )) :
            
            if grid[i][j] == 1:
                #(x,y,width,height)
                pygame.draw.rect(DISPLAYSURF, BLACK, ( h[j][i][0]-35, h[j][i][1] -35, 70,70) )
'''
    cx, cy 

    These are indices of centerx and centery
    Circle x-position, and yposition
'''
cx,cy = 0,0

def testCircleGrid():
    for i in centerx:
        for j in centery:
            drawCircle(i,j)

def putPathOnScreen(cx,cy, grid, goal, cost, heuristic):
    A_Star = search(grid,[cx,cy],goal,cost,heuristic)

    #commented out below is the beginning of a more efficient print function for this purpose
    '''

    delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

    x, y = cx, cy

    x2, y2 = x,y
    count = 1
    while x2 != goal[1] and y2 != goal[0]:
        count += 1
        if count > 200:
            return
        #x2, y2 = x,y
        nextSquare = [10000, x2, y2]
        for delt in delta:
            x2 = x + delt[0]
            y2 = y + delt[1]

            if x2 == goal[1] and y2 == goal[0]:
                print("got to the goal")
                return
            elif x2 < 0 or y2 < 0 or x2 > len(A_Star[0]) - 1 or y2 > len(A_Star) - 1:
                continue
            elif A_Star[y2][x2] == -1:
                continue
            elif A_Star[y2][x2] < nextSquare[0]:
                nextSquare = [ A_Star[y2][x2], x2, y2]

        x2, y2 = nextSquare[1], nextSquare[2]
    '''
    
    '''
    A_Star = np.array(A_Star)
    A_Star = np.transpose(A_Star)
    A_Star = list(A_Star)
    '''
    for i in range(len( grid ) ):
        for j in range( len(grid[0]) ):

            if A_Star[i][j] > 0:
                pygame.draw.rect(DISPLAYSURF, GREEN, ( h[j][i][0]-35, h[j][i][1] -35, 70,70) )
    return A_Star


while True: # the main game loop
    
    DISPLAYSURF.fill(WHITE)    
    DISPLAYSURF.blit(textSurfaceObject, textRectObj.center)

    drawGrid()
    putWallsOn()
    drawCircle(centerx[cx],centery[cy])
    putPathOnScreen(cy,cx, grid, goal, cost, heuristic)

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
        pprint(search(grid,[cy,cx],goal,cost,heuristic))
        #print(cx,cy)
    
    pygame.display.update()
    fpsClock.tick(FPS)