import pygame
import os


basePath = os.path.join("assets", "numbers")
defaultSize = (100, 100)
margin = 20
imgs = {}
strFilename = {"+": "plus", "-": "minus", "*": "times", "/": "divide", "=": "equal"}

for i in range(0, 10):
    imgs[str(i)] = pygame.transform.scale(
        pygame.image.load(os.path.join(basePath, f"{i}.png")), defaultSize
    )

for x in strFilename:
    imgs[x] = pygame.transform.scale(
        pygame.image.load(os.path.join(basePath, f"{strFilename[x]}.png")), defaultSize
    )

imgs["_"] = pygame.transform.scale(
    pygame.image.load(os.path.join(basePath, "blank.png")), defaultSize
)


def drawBlock(screen, block, x, y):
    screen.blit(imgs[block], (x, y))


def drawEquation(screen, eqString):
    w, h = screen.get_size()

    numBlocks = len(eqString)

    lenEquation = numBlocks * defaultSize[0] + (numBlocks - 1) * margin

    xCoord = (w - lenEquation) / 2
    yCoord = (h - defaultSize[1]) / 2

    posArr = []

    for i in range(len(eqString)):
        drawBlock(screen, eqString[i], xCoord, yCoord)
        xCoord += defaultSize[0] + margin
        posArr.append((xCoord, yCoord, defaultSize))

    return posArr
