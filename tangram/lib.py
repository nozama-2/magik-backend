import colours
import pygameclient
import copy
from time import sleep

root = 2**0.5

def init(plot):
	pygameclient.init(plot)

def quit():
	pygameclient.quit()

class Val():
	# Declaring a point as Art2 + B
	def __init__(self, A, B):
		self.A = A
		self.B = B

	def __float__(self):
		return self.A * root + self.B

	def __str__(self):
		if self.A == 0 and self.B == 0: return "0"
		elif self.A == 0: return str(self.B)
		elif self.B == 0: return f"{self.A}rt(2)"
		else: return f"{self.A}rt(2)+{self.B}"

	def __sub__(self, A):
		newA = self.A - A.A
		newB = self.B - A.B
		return Val(newA, newB)

	def __add__(self, A):
		newA = self.A + A.A
		newB = self.B + A.B
		return Val(newA,newB)

	def __eq__ (self, A):
		return self.A == A.A and self.B == A.B

	def __mul__(self,A):
		newA = self.A * A.B + self.B * A.A
		newB =  2 * self.A * A.A + self.B * A.B
		return Val(newA, newB)

	def div(self,A):
		return Val(self.A/A,self.B/A)

	def __lt__ (self,A): return float(self) < float(A)
	def __gt__ (self,A): return float(self) > float(A)
	def __le__ (self,A): return float(self) <= float(A)
	def __ge__ (self,A): return float(self) >= float(A)
		
class Point():
	# Coordinate (x,y) where x, y are both vals
	def __init__(self, x, y):
		if type(x) != Val or type(y) != Val:
			raise Exception("Invalid Coordinate")
		self.X = x
		self.Y = y

	def coord(self):
		return pygameclient.coord(float(self.X), float(self.Y))
	
	def __str__ (self):
		return f"({str(self.X)},{str(self.Y)})"

	def __eq__(self,A):
		if type(A) != Point: raise Exception ("Invalid Point")
		return self.X == A.X and self.Y == A.Y

	def __sub__(self,A):
		if type(A) != Point: raise Exception ("Invalid Point")
		newx = self.X - A.X
		newy = self.Y - A.Y
		return Point(newx,newy)

	def __add__(self,A):
		if type(A) != Point: raise Exception ("Invalid Point")
		newx = self.X + A.X
		newy = self.Y + A.Y
		return Point(newx,newy)

	def div(self,A):
		newx = self.X.div(A)
		newy = self.Y.div(A)
		return Point(newx,newy)

	def gradient(self):
		if float(self.X) == 0: return 1e9
		return float(self.Y) / float(self.X)

class Line():
	def __init__ (self, a, b):
		if type(a) != Point or type(b) != Point: 
			raise Exception ("Invalid Coordinate")
		self.A = a
		self.B = b
		self.lineAngle = lineAngle(self.A - self.B)

	def intersect(self, point):
		if type(point) != Point: raise Exception ("Invalid Point")
		# Don't count an intersection if points overlap
		if point == self.A or point == self.B:
			return 0

		if (point.X < self.A.X) and (point.X < self.B.X): return False
		if (point.Y < self.A.Y) and (point.Y < self.B.Y): return False
		if (point.X > self.A.X) and (point.X > self.B.X): return False
		if (point.Y > self.A.Y) and (point.Y > self.B.Y): return False

		# Intersection condition: LineAngle (A,P) == LineAngle(P,B)
		a = (self.A - point).gradient()
		b = (point - self.B).gradient()

		if abs(a-b) < 1e-3: return True
		return False

	def lineCross (self, line):
		if type(line) != Line: raise Exception ("Invalid Line")

		# Using CCW method: https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
		def ccw(A,B,C):
			return float(C.Y-A.Y) * float(B.X-A.X) > float(B.Y-A.Y) * float(C.X-A.X)

		return (self.A, line.A, line.B) != ccw(self.B, line.A, line.B)\
		and ccw(self.A, self.B, line.A) != ccw(self.A, self.B, line.B)

	def __str__ (self):
		return f"{str(self.A)}, {str(self.B)}"

class Shape():
	# Points is a list of coords
	def __init__(self, points):
		for p in points: 
			if type(p) != Point:
				raise Exception("Invalid Point")
		
		self.points = points
		self.N = len(self.points)
		self.area = self.calc_area()
		self.lines = []
		self.angles = []
		self.piece_type = 0

		for i in range(len(points)):
			self.angles.append({
				'point': points[i],
				'angles': calcAngles(i,self)
			})

		# Assigning piece type
		if self.N == 4:
			x = len(self.angles[0]['angles'])
			if x == 2:
				self.piece_type = 4 # Square
			else: 
				self.piece_type = 5 # Parallelogram
		else:
			if float(self.area) == 4.0: 
				self.piece_type = 1
			if float(self.area) == 2.0: 
				self.piece_type = 2
			if float(self.area) == 1.0: 
				self.piece_type = 3

		for i in range(len(points)):
			self.lines.append(Line(points[i-1], points[i]))

	def __str__(self):
		return 'Printing polygon: \n' + '\n'.join([str(i) for i in self.points])

	def drawShape(self,colour):
		colour = colours.getShapeColour(colour)
		coords = []
		for point in self.points:
			coords.append(point.coord())
		pygameclient.drawOutlines(colour, tuple(coords))

	def calc_area(self):
		# Retrurns the area of the shape through shoelace method
		A = Val(0,0)
		B = Val(0,0)
		for i in range(len(self.points)):
			A += self.points[i].X * self.points[i-1].Y
			B += self.points[i].Y * self.points[i-1].X
		area = A-B

		# Halve the area
		area.A /= 2
		area.B /= 2

		# If coordinates are in opposite direction
		if float(area) < 0:
			area.A = -area.A
			area.B = -area.B

		self.area = area

		return area

# Defining the 8 grid lines
dx = [1,1,1,0,-1,-1,-1,0]
dy = [-1,0,1,1,1,0,-1,-1]

def lineAngle(lineDelta):
	# Return an integer from 0 to 7 to give which sector line is in
	# Sectors are labelled clockwise (similar to clock) at 45deg segments
	# Takes in a line delta (difference between 2 points)

	X = float(lineDelta.X)
	Y = float(lineDelta.Y)
	
	# assert(abs(X - Y) == 0 or X * Y == 0)

	if X > 0 and Y < 0: return 0
	if X > 0 and Y == 0: return 1
	if X > 0 and Y > 0: return 2
	if X == 0 and Y > 0: return 3
	if X < 0 and Y > 0: return 4
	if X < 0 and Y == 0: return 5
	if X < 0 and Y < 0: return 6
	if X == 0 and Y < 0: return 7
	
	raise Exception("Invalid Line")

def calcAngles(index, shape):
	A = shape.points[index-1]
	B = shape.points[index]
	C = shape.points[(index+1) % shape.N]

	# Returns list of angles when the points A,B,C are continuous
	l1 = lineAngle(A - B)
	l2 = lineAngle(C - B)

	if l1 > l2: l1,l2 = l2,l1 # Keep l1 < l2# Keep l1 < l2
	# We first assume that it is acute
	if l2 - l1 <= 4:
		group1 = [i for i in range(l1+1, l2+1)]
	else:
		group1 = [i for i in range(l2+1,8)] + [i for i in range(0,l1+1)]

	# Want to determine if we should keep group 1 or use the opposite side
	# So we move in the direction of one of the group members
	# Check if the area increases or decreases

	area = shape.area

	# Extend one of the lines arbitrarily by a small amouint
	# If the arae decreases, then the angle is reflex

	delx = (dx[l2]) / 10
	dely = (dy[l2]) / 10
	# print("Change ",delx,dely)

	# Increment points[i]'s real portion by dx and dy respectively
	originalValue = shape.points[index]
	newValue = Point(
		Val(originalValue.X.A, originalValue.X.B - delx), 
		Val(originalValue.Y.A, originalValue.Y.B - dely) 
	)
	shape.points[index] = newValue
	newarea = shape.calc_area()
	shape.points[index] = originalValue
	shape.area = area

	# print("Area: ",area,float(newarea))
	if float(newarea) < float(area):
		# Should be convex, swap
		group1 = [i for i in range(0,8) if i not in group1]
	
	return group1

def LineDirection(index, shape):
	# Uses angles of adjacent indexes to find out which 4 angles are resolved by the line
	# Line is drawn from index-1 to index

	# The size-4 set of angles will be the set that contains both left and right angles
	left_angles = calcAngles(index-1, shape)
	right_angles = calcAngles(index,shape)
	line_angle = lineAngle(shape.points[index] - shape.points[index-1])
	line_angle2 = (line_angle + 4)%8
	top = max(line_angle, line_angle2)

	group1 = [i for i in range(top, top-4, -1)]
	if left_angles[0] not in group1:
		group1 = [i for i in range(0,8) if i not in group1]

	return group1

class Puzzle():
	def __init__(self, points):
		for p in points: 
			if type(p) != Point:
				raise Exception("Invalid Point")

		self.points = copy.deepcopy(points)
		self.outlinePoints = copy.deepcopy(points)
		self.angles = []
		self.shape = Shape(copy.deepcopy(points))
		self.lines = []
		self.addedShapes = []
		self.complexity = 0
		self.status = "Correct"

		for i in range(len(points)):
			self.angles.append({
				'point': points[i],
				'angles': calcAngles(i,self.shape)
			})

		for i in range(len(points)):
			self.lines.append(Line(points[i-1], points[i]))

		# Centralise drawing
		pygameclient.calibrate(self.outlinePoints)
		
		# self.updatePygame()

	def drawPuzzle(self):
		# Draw main shape
		coords = []
		for point in self.outlinePoints:
			coords.append(point.coord())
			
		pygameclient.drawOutlines(colours.gray, tuple(coords))
		drawn_pieces = []
		
		# Draw shapes
		for shape in self.addedShapes:
			# Then you are the second one being draw
			colour = shape.piece_type
			if colour in drawn_pieces: # Re-map colours
				if colour == 1: colour = 6
				if colour == 3: colour = 7

			shape.drawShape(colour=colour)
			drawn_pieces.append(colour)

		# Write coordinate texts
		for angle in self.angles:
			point = angle['point']
			coord = point.coord()
			pygameclient.labelText(coord, angle['angles'])

	def __str__(self):
		output = "Printing puzzle:\n"
		for coord in self.angles:
			output += f"{coord['point']}: {coord['angles']}\n"
		return output

	def addShape(self,shape):
		areaFloat = float(shape.area)

		if abs(int(areaFloat) - areaFloat) > 1e-5:
			raise Exception("Invalid Shape Area")

		self.addedShapes.append(shape)

		for i in range(len(shape.points)):
			point = shape.points[i]

			if point in self.points:
				# First case, there is point overlap

				ind = self.points.index(point)
				resolved_angles = calcAngles(i, shape)
				original_angles = self.angles[ind]['angles']
				new_angles = [i for i in original_angles if i not in resolved_angles]
				
				if len(original_angles) != len(new_angles) + len(resolved_angles):
					raise Exception(f"Invalid angle at point {point}")

				self.angles[ind]['angles'] = new_angles

			else:
				# Create a new point. 
				# Check if the point lies on a pre-existing line
				# print(f"Creating new point {point}")

				resolved_angles = calcAngles(i,shape)
				angles = [i for i in range(0,8)]

				# Check if this point is intersected by any existing line
				for j in range(len(self.lines)):
					line = self.lines[j]

					if line.intersect(point):
						# Only neeed angles inside main shape
						line_angle = lineAngle(line.A - line.B)
						line_angle2 = (line_angle + 4)%8
						top = max(line_angle, line_angle2)

						angles = [i for i in range(top, top-4, -1)]
									
				# Flip angles to other side (since our made shape may have convex)
				if resolved_angles[0] not in angles:
					angles = [i for i in range(0,8) if i not in angles]
				
				angles = [i for i in angles if i not in resolved_angles]
				
				self.points.append(point)
				self.angles.append({
					'point': point,
					'angles': angles
				})
				pass
				# print("Outside")

		for i in range(len(shape.lines)):
			line = shape.lines[i]

			# Check if new line intersects existing point
			
			for j in range(len(self.angles)):
				angle = self.angles[j]

				if line.intersect(angle['point']):
					resolved_angles = LineDirection(i, shape)
					original_angles = angle['angles']
					new_angles = [i for i in original_angles if i not in resolved_angles]
					if len(original_angles) != len(new_angles) + len(resolved_angles):
						raise Exception(f"Invalid angle at point {point}")

					self.angles[j]['angles'] = new_angles

		for line in shape.lines:
			self.lines.append(copy.deepcopy(line))

		# self.updatePygame()

	def updatePygame(self):

		pygameclient.calibrate(self.points)
		pygameclient.plot(self)
