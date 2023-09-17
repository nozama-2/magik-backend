import pygame
from pygame.locals import *

from myUtils.equation import *
from myUtils.draw import *
from classes.equation import *

white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
gray = (0, 0, 0)
# gray = (107, 107, 107)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_size()

clock = pygame.time.Clock()

pygame.display.set_caption("Equations")

exit = False

hintStartTime = -1e99
corrStartTime = -1e99
wrongStartTime = -1e99
currTime = 0

equation = Equation(screen, 100, 20)

clicked = None
bgColor = gray

# Font
font = pygame.font.Font(None, 32)
midScreenText = ""
midScreenPos = (w // 2, h // 2)

print(equation.ansEquation, equation.currEq)

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        # Hint screen
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mPos = pygame.mouse.get_pos()
            clicked = equation.getClicked(mPos[0], mPos[1])

        elif event.type == pygame.KEYDOWN:
            text = event.unicode
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            elif text in "0123456789pmtd":
                opDict = {
                    "p": "+",
                    "m": "-",
                    "t": "*",
                    "d": "/",
                }
                if text in "pmtd":
                    midScreenText = opDict[midScreenText]

                new = list(equation.currEq)
                if clicked != None:
                    i = equation.blocks.index(clicked)
                else:
                    i = equation.currEq.index("_")
                new[i] = text
                equation.currEq = "".join(new)

            elif event.key == pygame.K_SPACE:
                equation.renderHint()
                bgColor = orange
                hintStartTime = currTime

    screen.fill(bgColor)

    # text blit
    midscreenTextElem = font.render(midScreenText, True, black)
    textRect = midscreenTextElem.get_rect()
    textRect.center = midScreenPos
    screen.blit(midscreenTextElem, textRect)

    equation.displayEquation()

    # Flashes hint screen momentarily
    if currTime - hintStartTime > 3000:
        equation.unrenderHint()
        bgColor = gray

    # Flashes correct screen momentarily
    if currTime - corrStartTime < 5000:
        equation.hide = True
        bgColor = green
        midScreenText = "Correct! Please remove pieces from board"
    # Flashes wrong screen momentarily
    elif currTime - wrongStartTime < 5000:
        bgColor = red
        midScreenPos = (w // 2, h // 2 - 100)
        midScreenText = "Ohno... Remove pieces and try again!"
    else:
        equation.hide = False
        midScreenText = ""

    if equation.isFilled():
        if equation.isCorrect():
            equation.hide = True
            corrStartTime = currTime
            equation.reset()
        else:
            wrongStartTime = currTime
            print(equation.questionEquation)
            equation.updateDisplayedEquation(equation.questionEquation)
            equation.currEq = equation.questionEquation

    pygame.display.update()

    currTime += 60
    clock.tick(60)

pygame.quit()
quit()
