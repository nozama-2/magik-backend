from lib import *
import copy
from time import sleep
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
		targetAngles = target['angles']
		actualAngles = [min(targetAngles)]
		templateShape = self.orientations[index]

		while (actualAngles[-1] + 1) % 8 in targetAngles:
			actualAngles.append((actualAngles[-1] + 1) % 8 )
		actualAngles = set(actualAngles)
		# Actual angles is longest consec that begins at lowest missing 
		# print("Target Angles", actualAngles)

		targetIndex = -1
		for i in range(len(templateShape.angles)):
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

		# Get push all points towards center (slightly smaller) to exclude point intersections
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

# Medium Triangle
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

# Small Triangle
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

# Square
piece4 = TemplatePiece(
	type = 4,
	orientations = [
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,0), Val(1,0)), Point(Val(1,0), Val(1,0)),Point(Val(1,0), Val(0,0))]),
		Shape([Point(Val(0,0), Val(0,0)), Point(Val(0,-1), Val(0,1)), Point(Val(0,0), Val(0,2)),Point(Val(0,1), Val(0,1))])
	]
)

# Parallelogram
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
    Point(Val(0,0), Val(0,4)),
    Point(Val(0,4), Val(0,4)),
    Point(Val(0,4), Val(0,0))
]

# points = [
#     Point(Val(0,0), Val(0,0)),
#     Point(Val(1,0), Val(0,0)),
#     Point(Val(1,0), Val(1,1.5)),
#     Point(Val(1,1), Val(1,0.5)),
#     Point(Val(1,2), Val(1,1.5)),
#     Point(Val(2,1), Val(0,2.5)),
#     Point(Val(4,1), Val(2,2.5)),
#     Point(Val(3,1), Val(2,2.5)),
#     Point(Val(3,1), Val(3,2.5)),
#     Point(Val(1,2), Val(1,3.5)),
#     Point(Val(1,0), Val(1,5.5)),
#     Point(Val(1,0), Val(1,2)),
#     Point(Val(1,-1), Val(1,1)),
#     Point(Val(1,-1), Val(1,-1))
# ]

# points = [
#     Point(Val(1,0), Val(0,0)),
#     Point(Val(0,0), Val(1,0)),
#     Point(Val(1,0), Val(1,0)),
#     Point(Val(1,0), Val(3,0)),
#     Point(Val(2,0), Val(4,0)),
#     Point(Val(2,0), Val(3,0)),
#     Point(Val(4,0), Val(3,0)),
#     Point(Val(4,2), Val(3,-2)),
#     Point(Val(4,2), Val(2,-2)),
#     Point(Val(3,2), Val(3,-2)),
#     Point(Val(4,-2), Val(3,-2))
# ]

P = Puzzle(points)
P.drawPuzzle()
placed_pieces = 0
current_pieces = []
complexity = 0
solved = 0

def solve(Puzzle):
	global placed_pieces, complexity, solved
	if solved == 1: return

	if placed_pieces == 7:
		# Solved
		solved = 1
		Puzzle.status = "Correct"
		Puzzle.updatePygame()
		return

	Puzzle.updatePygame()
	
	# Select index to be point with fewest angles remaining
	weights = [len(x['angles']) for x in Puzzle.angles]
	for i in range(len(weights)): 
		if weights[i] == 0: weights[i] = 1e9

	index = min(range(len(weights)), key=lambda x:weights[x])
	fit_pieces = []

	for piece in pieces:
		if pieceCount[piece.type] == 0:
			continue
		fit_pieces += piece.fitAll(Puzzle,index)

	complexity += len(fit_pieces)

	print("Placed ",placed_pieces)
	print("Fit ",len(fit_pieces))

	if len(fit_pieces) == 0: 
		Puzzle.updatePygame()
		return False

	for i in range(len(fit_pieces)):
		new_puzzle = copy.deepcopy(Puzzle)
		try:
			new_puzzle.addShape(fit_pieces[i]['shape'])
		except: 
			fit_pieces[i]['failed'] = True
		fit_pieces[i]['new_puzzle'] = new_puzzle
		fit_pieces[i]['score'] = sum([len(x['angles']) for x in new_puzzle.angles])

	fit_pieces = [i for i in fit_pieces if 'failed' not in i]
	fit_pieces.sort(key=lambda i:i['score'])
	rng = []
	N = len(fit_pieces)
	for i in range(N):
		rng += [i]

	rng.reverse()
	unique_indexes = []
	for i in rng: 
		if i not in unique_indexes: unique_indexes.append(i)

	for i in range(N):
		piece_index = unique_indexes[i]
		placed_pieces += 1
		piece_type = fit_pieces[piece_index]['type']
		pieceCount[piece_type] -= 1

		# print(fit_pieces[0]['shape'])
		solve(fit_pieces[piece_index]['new_puzzle'])

		# Failed
		placed_pieces -= 1
		pieceCount[piece_type] += 1

if __name__ == '__main__':
	solve(P)
