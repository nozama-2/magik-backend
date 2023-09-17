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
red = (255,0,0)

shapes = [darkGreen,lightGreen,pink,yellow,blue,orange,purple]
index = 0
# shapes = [orange,darkGreen]

def getShapeColour(index):
	return shapes[index-1]

def resetIndex():
	index = 0