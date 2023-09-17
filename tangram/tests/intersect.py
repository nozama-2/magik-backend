from lib import *
import copy

def run_test():
	init(plot=False)

	A = Point(Val(0,0), Val(0,0))
	B = Point(Val(0,0), Val(0,1))
	C = Point(Val(0,1), Val(0,0))
	D = Point(Val(0,1), Val(0,1))
	E = Point(Val(0,0.5), Val(0,0))
	F = Point(Val(0,0.5), Val(0,0.5))
	G = Point(Val(0.5,0), Val(0.5,0))

	L1 = Line(A,D)
	L2 = Line(A,C)
	print(L1.intersect(G))
	print(L1.intersect(F))
	print(L1.intersect(E))
	print(L2.intersect(E))

# Should be True, False, False, False
run_test()