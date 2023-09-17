from lib import *
import copy
# Use copy.deepcopy to duplicate entire item

def run_test():
    init(plot=False)

    points = [
        Point(Val(0,0), Val(0,0)),
        Point(Val(0,0), Val(0,4)),
        Point(Val(0,4), Val(0,4)),
        Point(Val(0,4), Val(0,0))
    ]

    P = Puzzle(points)
    P.drawPuzzle()
    print(P)