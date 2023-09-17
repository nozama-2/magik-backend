import pygame
import os


def getImgPaths(defaultSize):
    basePath = os.path.join(os.getcwd(), "assets", "numbers")
    imgs = {}
    strFilename = {"+": "plus", "-": "minus", "*": "times", "/": "divide", "=": "equal"}

    for i in range(0, 10):
        imgs[str(i)] = pygame.transform.scale(
            pygame.image.load(os.path.join(basePath, f"{i}.png")),
            (defaultSize, defaultSize),
        )

    for x in strFilename:
        imgs[x] = pygame.transform.scale(
            pygame.image.load(os.path.join(basePath, f"{strFilename[x]}.png")),
            (defaultSize, defaultSize),
        )

    imgs["_"] = pygame.transform.scale(
        pygame.image.load(os.path.join(basePath, "blank.png")),
        (defaultSize, defaultSize),
    )

    return imgs
