import pygame, time
from pygame.locals import *

black = (0, 0, 0)
white = (200, 200, 200)
pink = (255, 117, 118)
purple = (217, 155, 255)
blue = (0, 0, 255)
yellow = (255, 205, 31)
orange = (255, 137, 0)
lightGreen = (100, 255, 203)
darkGreen = (1, 128, 32)
successGreen = (156, 255, 124)
gray = (128,128,128)

windowWidth = 720
windowHeight = 720


def drawGrid():
    global marginLeft, marginTop, blockSize
    blockSize = 30 #Set the size of the grid block 
    # block size 30 is for 24 x 24 grid
    # block size 60 for 12 x 12 grid

    screenX, screenY = screen.get_size()
    # print(screenX, screenY)
    marginLeft = (screenX - windowWidth) / 2 
    marginTop = (screenY - windowHeight) / 2
    for x in range(0, windowWidth, blockSize):
        for y in range(0, windowHeight, blockSize):
            rect = pygame.Rect(marginLeft + x, marginTop+ y, blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)


def coord(X,Y):
    return (marginLeft + X *2* blockSize, marginTop+Y*blockSize*2)

def drawOutlines(screen, colour, coordSet):
    pygame.draw.polygon(screen, colour, coordSet)
    pygame.draw.polygon(screen, black, coordSet, 2)

def main():
    global screen, clock, screenSize
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # screen = pygame.display.set_mode((windowWidth, windowHeight))
    clock = pygame.time.Clock()
    screen.fill(black)
    # drawGrid()
    
    # pygame.draw.polygon(screen, (255, 117, 118), ((marginLeft, marginTop), (marginLeft+ 6*blockSize, marginTop+ 6*blockSize), (marginLeft, marginTop+12*blockSize)))
    screenColour = black

    while True:
        screen.fill(screenColour) # comment this out in order for the display of shapes to be permanent
        drawGrid()
        if screenColour == successGreen:
            time.sleep(0.2)
        screenColour = black

        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]: #simulating daniel's websocket pushing data over to me
            drawOutlines(screen, pink, (coord(0, 0), coord(6, 6), coord(0, 12))) 
        if keys[pygame.K_2]:
            drawOutlines(screen, purple, (coord(0, 0), coord(6, 6), coord(12, 0)))
        if keys[pygame.K_3]:
            drawOutlines(screen, blue, (coord(9, 3), coord(6, 6), coord(9, 9)))
        if keys[pygame.K_4]: 
            drawOutlines(screen, yellow, (coord(9, 3), coord(12, 0), coord(12, 6), coord(9, 9)))
        if keys[pygame.K_5]:   
            drawOutlines(screen, orange, (coord(6, 12), coord(12, 12), coord(12, 6)))
        if keys[pygame.K_6]:    
            drawOutlines(screen, lightGreen, (coord(6, 6), coord(9, 9), coord(6, 12), coord(3, 9)))
        if keys[pygame.K_7]:
            drawOutlines(screen, darkGreen, (coord(6, 12), coord(0, 12), coord(3, 9)))

         #simulating daniel's websocket pushing data over to me
        drawOutlines(screen, pink, (coord(0, 0), coord(6, 6), coord(0, 12))) 
    
        drawOutlines(screen, purple, (coord(0, 0), coord(6, 6), coord(12, 0)))
    
        drawOutlines(screen, blue, (coord(9, 3), coord(6, 6), coord(9, 9)))
        
        drawOutlines(screen, yellow, (coord(9, 3), coord(12, 0), coord(12, 6), coord(9, 9)))
        
        drawOutlines(screen, orange, (coord(6, 12), coord(12, 12), coord(12, 6)))
        
        drawOutlines(screen, lightGreen, (coord(6, 6), coord(9, 9), coord(6, 12), coord(3, 9)))
    
        drawOutlines(screen, darkGreen, (coord(6, 12), coord(0, 12), coord(3, 9)))


        # drawOutlines(screen, pink, (coord(0, 0), coord(6, 6), coord(0, 12))) 
        # drawOutlines(screen, purple, (coord(0, 0), coord(6, 6), coord(12, 0)))
        # drawOutlines(screen, blue, (coord(9, 3), coord(6, 6), coord(9, 9)))
        # drawOutlines(screen, yellow, (coord(9, 3), coord(12, 0), coord(12, 6), coord(9, 9)))
        # drawOutlines(screen, orange, (coord(6, 12), coord(12, 12), coord(12, 6)))
        # drawOutlines(screen, lightGreen, (coord(6, 6), coord(9, 9), coord(6, 12), coord(3, 9)))
        # drawOutlines(screen, darkGreen, (coord(6, 12), coord(0, 12), coord(3, 9)))

        # for event in

        if keys[pygame.K_9]:
            screenColour = successGreen
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()
        clock.tick(60)


main()