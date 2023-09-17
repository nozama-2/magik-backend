import pygame
from myUtils.getImgPaths import *


class Block:
    def __init__(self, x, y, screen, data, size):
        self.x = x
        self.y = y
        self.size = size
        self.margin = 20
        self.screen = screen
        self.data = data
        self.imgs = getImgPaths(size)
        self.selected = False

    def isIn(self, xPos, yPos):
        return (
            xPos >= self.x
            and xPos <= self.x + self.size
            and yPos >= self.y
            and yPos <= self.y + self.size
        )

    def drawBlock(self):
        self.screen.blit(self.imgs[self.data], (self.x, self.y))
