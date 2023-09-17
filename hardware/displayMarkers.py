
import pygame, time
from pygame.locals import *
import os
import numpy as np

black = (0, 0, 0)
white = (255, 255, 255)
pink = (255, 117, 118)
purple = (217, 155, 255)
blue = (136, 149, 255)
yellow = (255, 205, 31)
orange = (255, 137, 0)
lightGreen = (100, 255, 203)
darkGreen = (45, 217, 152)
successGreen = (156, 255, 124)



fullPath = os.path.join(os.path.dirname(__file__), 'markers')
fileList = os.listdir(fullPath)

# markersPath = [f"images/{name}" for name in fileList]
markersPath = [os.path.join(fullPath, name) for name in fileList]
markersPath = sorted(markersPath)

# print(markersPath)

markers = []
for i in markersPath:
    markers.append(pygame.image.load(i))

windowWidth = 1200
windowHeight = 800

def drawGrid():
    global marginLeft, marginTop, blockSize
    blockSize = 200 #Set the size of the grid block 
    # block size 30 is for 24 x 24 grid
    # block size 60 for 12 x 12 grid

    screenX, screenY = screen.get_size()
    # print(screenX, screenY)
    marginLeft = (screenX - windowWidth) / 2 
    marginTop = (screenY - windowHeight) / 2
    padding = 25
    id = 0

    points = []
    for x in range(0, windowWidth, blockSize):
        for y in range(0, windowHeight, blockSize):
            rectOutline = pygame.Rect(marginLeft + x, marginTop+ y, blockSize, blockSize)
            image = markers[id]    

            rect = image.get_rect(center=(marginLeft + x + blockSize / 2, marginTop + y + blockSize / 2))
            
            screen.blit(image, rect)

            # rect = pygame.Rect(left)

            pygame.draw.rect(screen, black, rectOutline, 1)
            id += 1
            points.append([x+padding+marginLeft, y+padding+marginTop])  # top left
            points.append([x+padding+marginLeft+150, y+padding+marginTop])  # top right
            points.append([x+padding+marginLeft+150, y+padding+marginTop+150])  # bottom right
            points.append([x+padding+marginLeft, y+padding+marginTop+150])  # bottom left
            
            # break

    points = np.array(points)
    with open('points.txt','w') as file:
        file.writelines(f"{points}")

    print(points)

def main():
    global screen, clock, screenSize
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((windowWidth, windowHeight))

    clock = pygame.time.Clock()
    screen.fill(white)
    # drawGrid()

    screenColour = white

    while True:
        screen.fill(screenColour) 
        drawGrid()


        keys = pygame.key.get_pressed()


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