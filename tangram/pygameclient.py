import pygame, time
from pygame.locals import *
import colours
import sys

windowWidth = 720
windowHeight = 720
PLOT=True

def init(plot):
	global marginLeft, marginTop, blockSize, screen, clock, screenSize

	global PLOT
	if plot == False:
		PLOT=False
	# 	return

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

	screen.fill(colours.black) # comment this out in order for the display of shapes to be permanent
	
	blockSize = 90 #Set the size of the grid block 
	# block size 30 is for 24 x 24 grid
	# block size 60 for 12 x 12 grid

	screenX, screenY = screen.get_size()
	marginLeft = (screenX - windowWidth) / 2 
	marginTop = (screenY - windowHeight) / 2

deltX = 0
deltY = 0
def calibrate(points):
	global deltX, deltY
	# print("")
	# for i in points: print(i)

	X = [float(point.X) for point in points]
	maxX = max(X)
	minX = min(X)
	deltX = (8 - (maxX - minX)) / 2
	deltX = deltX - minX

	Y = [float(point.Y) for point in points]
	maxY = max(Y)
	minY = min(Y)
	deltY = (6 - (maxY - minY)) / 2
	deltY = deltY - minY

	print(deltX, deltY)
	# deltX = deltY = 0

def coord(X,Y):
	# Perform calibration
	global deltX, deltY
	X += deltX 
	Y += deltY

	return (marginLeft + X *blockSize, marginTop+Y*blockSize)

def drawOutlines(colour, coordSet):
	global screen

	pygame.draw.polygon(screen, colour, coordSet)
	pygame.draw.polygon(screen, colours.black, coordSet, 2)

def labelText(coord, data):
	if len(data) == 0:
		pygame.draw.circle(screen, colours.successGreen, coord, 8)
	else:
		pygame.draw.circle(screen, colours.red, coord, 10)
		font = pygame.font.SysFont('roboto', 28)
		# return
		img1 = font.render(str(data), True, (255, 255, 255))
		screen.blit(img1, coord)

def plot(Puzzle):
	screen.fill(colours.black)

	Puzzle.drawPuzzle()
	caption = f"Status: {Puzzle.status}"
	font = pygame.font.SysFont('roboto', 72)
	img1 = font.render(str(caption), True, colours.white)
	if Puzzle.status == 'Incorrect':
		screen.blit(img1, coord(1.45,7.2))
	else:
		screen.blit(img1, coord(1.5,7.2))

	pygame.display.update()
	clock.tick(60)
	time.sleep(0.05)

def save(filename):
	global windowWidth,windowHeight,screen
	# screenshot = pygame.Surface((windowHeight,windowWidth))
	# screenshot.blit(screen, coord(0, 0))
	pygame.image.save(screen, filename)
	print(f"Saved screenshot as '{filename}'")
	
def quit():
	pygame.quit()
	print("Quit!")
	sys.exit()


