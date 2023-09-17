from lib import *
import copy
from time import sleep
from pygameclient import save
from sys import exit
from random import choice,shuffle

class TemplatePiece():
	def __init__(self,type,orientations):
		self.type = type
		self.orientations = orientations

	def match(self, puzz, target, index):
		# We matching coordinates[index] to point
		# Automatically chooses which coordinate based on whats available
		# This works because each coordinate can only overlap with an angle 1 time
		# And some person must be able to match each angle

		targetPoint = target['point']
		# print(targetPoint)
		targetAngles = target['angles']
		# actualAngles = [min(targetAngles)]
		actualAngles = [choice(targetAngles)]
		templateShape = self.orientations[index]

		while (actualAngles[-1] + 1) % 8 in targetAngles:
			actualAngles.append((actualAngles[-1] + 1) % 8 )
			if len(actualAngles) == 8: break

		actualAngles = set(actualAngles)
		# Actual angles is longest consec that begins at lowest missing 
		# print("Target Angles", actualAngles)
		# print(templateShape)

		targetIndex = -1
		for i in range(len(templateShape.angles)):
			# print(templateShape.angles[i]['angles'])
			# if actualAngles.issubset(set(templateShape.angles[i]['angles'])):

			# Must match minimum + be subset of angles
			if min(templateShape.angles[i]['angles']) == min(actualAngles):
				if set(templateShape.angles[i]['angles']).issubset(set(actualAngles)):
					targetIndex = i
					break

		# print(targetIndex)
		if targetIndex == -1: return False

		# Current shape is template shape but displaced to coordinates
		offset = targetPoint - templateShape.points[targetIndex]
		currPoints = [point+offset for point in templateShape.points]

		# Get smaller version of currShape
		# Then check for any intersections
		centerSum = Point(Val(0,0), Val(0,0))
		for point in currPoints: centerSum += point
		center = centerSum.div(len(currPoints))

		smallPoints = [
			(point.div(0.1) + center).div(11) for point in currPoints
		]

		currShape = Shape(currPoints)
		smallShape = Shape(smallPoints)

		# print(currShape)
		# print(smallShape)

		for lineA in puzz.lines:
			for lineB in smallShape.lines:
				if lineA.lineCross(lineB) and lineB.lineCross(lineA):
					# print("INTERSECT ",lineA, lineB)
					# print(lineB.lineCross(lineA))
					# print(float(lineA.A.X), float(lineA.A.Y))
					# print(float(lineA.B.X), float(lineA.B.Y))
					# print(float(lineB.A.X), float(lineB.A.Y))
					# print(float(lineB.B.X), float(lineB.B.Y))
					return False

		return {'shape': currShape, 'type': self.type}

	# Tries to put all orientations into target index
	def fitAll(self,puzz,targetIndex):
		fitPieces = []
		for i in range(len(self.orientations)):
			res = self.match(puzz,puzz.angles[targetIndex], i)
			if res: fitPieces.append(res)
		return fitPieces

# Big Traingle
pieces = []
piece1 = TemplatePiece(
	type = 1,
	orientations = [
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(2,0)), Point(Val(2,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(-2,0)), Point(Val(2,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(2,0)), Point(Val(-2,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(-2,0)), Point(Val(-2,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-2), Val(0,-2)), Point(Val(0,-2),Val(0,2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-2), Val(0,2)), Point(Val(0,2),Val(0,2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,2), Val(0,2)), Point(Val(0,2),Val(0,-2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,2), Val(0,-2)), Point(Val(0,-2),Val(0,-2))])
	]
)

piece2 = TemplatePiece(
	type = 2,
	orientations = [
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,2), Val(0,0)), Point(Val(0,0), Val(0,2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-2), Val(0,0)), Point(Val(0,0), Val(0,2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,2), Val(0,0)), Point(Val(0,0), Val(0,-2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-2), Val(0,0)), Point(Val(0,0), Val(0,-2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(-1,0), Val(-1,0)), Point(Val(-1,0), Val(1,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(-1,0), Val(1,0)), Point(Val(1,0), Val(1,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(1,0), Val(1,0)), Point(Val(1,0), Val(-1,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(1,0), Val(-1,0)), Point(Val(-1,0), Val(-1,0))])
	]
)

piece3 = TemplatePiece(
	type = 3,
	orientations = [
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(1,0)), Point(Val(1,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(-1,0)), Point(Val(1,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(1,0)), Point(Val(-1,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(-1,0)), Point(Val(-1,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-1), Val(0,-1)), Point(Val(0,-1),Val(0,1))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-1), Val(0,1)), Point(Val(0,1),Val(0,1))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,1), Val(0,1)), Point(Val(0,1),Val(0,-1))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,1), Val(0,-1)), Point(Val(0,-1),Val(0,-1))])
	]
)

piece4 = TemplatePiece(
	type = 4,
	orientations = [
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(1,0)), Point(Val(1,0), Val(1,0)),Point(Val(1,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-1), Val(0,1)), Point(Val(0,0), Val(0,2)),Point(Val(0,1), Val(0,1))])
	]
)

piece5 = TemplatePiece(
	type = 5,
	orientations = [
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,1), Val(0,-1)), Point(Val(0,1), Val(0,1)),Point(Val(0,0), Val(0,2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-1), Val(0,-1)), Point(Val(0,-1), Val(0,1)),Point(Val(0,0), Val(0,2))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,1), Val(0,-1)), Point(Val(0,3), Val(0,-1)),Point(Val(0,2), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,1), Val(0,1)), Point(Val(0,3), Val(0,1)),Point(Val(0,2), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(1,0)), Point(Val(1,0), Val(2,0)),Point(Val(1,0), Val(1,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(1,0)), Point(Val(-1,0), Val(2,0)),Point(Val(-1,0), Val(1,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(1,0), Val(0,0)), Point(Val(2,0), Val(1,0)),Point(Val(1,0), Val(1,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(1,0), Val(0,0)), Point(Val(2,0), Val(-1,0)),Point(Val(1,0), Val(-1,0))])
	]
)

pieces = [piece1, piece2, piece3, piece4, piece5]

pieceCount = {
	1:2,
	2:1,
	3:2,
	4:1,
	5:1
}

init(plot=False)

points = [
    Point(Val(0,0), Val(0,0)),
    Point(Val(0,0), Val(0,16)),
    Point(Val(0,16), Val(0,16)),
    Point(Val(0,16), Val(0,0))
]

P = Puzzle(points)
P.points.append(Point(Val(0,8), Val(0,8)))
P.angles.append({
	'point': Point(Val(0,8), Val(0,8)),
	'angles': [i for i in range(0,8)]
})


P.drawPuzzle()
placed_pieces = 0
current_pieces = []
solved = 0

def generate(Puzzle,fileIndex):
	global placed_pieces, solved
	Puzzle.updatePygame()

	if solved: return

	if placed_pieces == 7:
		# Finished generation
		solved = 1
		Puzzle.updatePygame()
		save(f'image{fileIndex}.jpg')
		sleep(2)
		return

	# Select index to be point with fewest angles remaining
	weights = [len(x['angles']) for x in Puzzle.angles]
	for i in range(len(weights)): 
		if weights[i] == 0: weights[i] = 1e9

	# Skip outer points
	index = min(range(4,len(weights)), key=lambda x:weights[x])
	fit_pieces = []
	print(index)

	for piece in pieces:
		if pieceCount[piece.type] == 0:
			continue
		fit_pieces += piece.fitAll(Puzzle,index)

	print("Placed ",placed_pieces)
	print("Fit ",len(fit_pieces))

	if len(fit_pieces) == 0: 
		return False

	for i in range(len(fit_pieces)):
		new_puzzle = copy.deepcopy(Puzzle)
		new_puzzle.addShape(fit_pieces[i]['shape'])
		fit_pieces[i]['new_puzzle'] = new_puzzle
		fit_pieces[i]['score'] = sum([len(x['angles']) for x in new_puzzle.angles])

	fit_pieces.sort(key=lambda i:i['score'])
	rng = []
	N = len(fit_pieces)
	for i in range(N):
		rng += (N-i) * [i]

	shuffle(rng)

	for i in range(N):
		piece_index = rng[i]

		placed_pieces += 1
		piece_type = fit_pieces[piece_index]['type']
		pieceCount[piece_type] -= 1

		# print("Putting piece")
		# print(fit_pieces[0]['shape'])
		generate(fit_pieces[piece_index]['new_puzzle'],fileIndex)

		# Failed
		placed_pieces -= 1
		pieceCount[piece_type] += 1

for i in range(100):
	solved = 0
	generate(P,i)
	sleep(2)
