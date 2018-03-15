'''
Made by Lucas working through Al Swiegart's book, Making Games with Python & Pygame

'''
import pygame, sys
from pygame.locals import *
pygame.init()
from ArtPieUtils import *

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#this will make the grid, 4x4
gridSize = 4

#grid line width
gridLineWidth = 4

width = 400
height = 400
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('A Grid')

anImg = pygame.image.load('anImg.png')
redBallx = 10
redBally = 10

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObject = fontObj.render ("Hi, Lucas", True, GREEN, BLUE)
textRectObj = textSurfaceObject.get_rect()
textRectObj.center = (200,150)

def drawCircle(x,y):
    #circle(Surface, color, pos, radius, width=0) 0 width means it'll filled
    pygame.draw.circle(DISPLAYSURF, RED, (x,y), width // gridSize // 3 )

DISPLAYSURF.fill(WHITE)
#draw vertical lines
centerx = []
centery = []
increment = width // gridSize

#should be
# 50, 152, 258
prevCoordx = 4
for i in range(0,width , increment):
    

    centerx.append((prevCoordx + increment//2 ) )
    pygame.draw.line(DISPLAYSURF, BLUE, (i, 0), (i, height), gridLineWidth)
    prevCoordx += increment# + gridLineWidth

#draw horizontal lines
prevCoordy = 4
for i in range(0,height, increment):
    print("prevCoordy",prevCoordy,i)
    centery.append(prevCoordy + (increment)//2 )
    pygame.draw.line(DISPLAYSURF, BLUE, (0, i), (width, i), gridLineWidth)
    prevCoordy += increment# + gridLineWidth
print(len(centery), centery)

def drawGrid():
    for i in range(0,height, increment):
        pygame.draw.line(DISPLAYSURF, BLUE, (i, 0), (i, height), gridLineWidth)
        pygame.draw.line(DISPLAYSURF, BLUE, (0, i), (width, i), gridLineWidth)


'''
    cx, cy 

    These are indices of centerx and centery
    Circle x-position, and yposition
'''
cx,cy = 0,0

while True: # the main game loop
    
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(anImg, (redBallx, redBally))
    DISPLAYSURF.blit(textSurfaceObject, textRectObj.center)
    drawGrid()

    '''
    for i in centery:
        for j in centerx:
            drawCircle(i,j)
    '''

    drawCircle(centerx[cx],centery[cy])

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
    '''
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_UP]:
        redBally -= 5
    elif keys[pygame.K_DOWN]:
        redBally += 5
    elif keys[pygame.K_RIGHT]:
        redBallx += 5
    elif keys[pygame.K_LEFT]:
        redBallx -= 5 
    elif keys[pygame.K_x]:
        quitFunc()
    '''

    pygame.display.update()
    fpsClock.tick(FPS)