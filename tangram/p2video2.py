from lib import *
import copy
# Use copy.deepcopy to duplicate entire item
import solver_rng
from time import sleep

def run_test():
    init(plot=True)

    points = [
        Point(Val(0,0), Val(0,0)),
        Point(Val(1,0), Val(0,0)),
        Point(Val(1,0), Val(1,1.5)),
        Point(Val(1,1), Val(1,0.5)),
        Point(Val(1,2), Val(1,1.5)),
        Point(Val(2,1), Val(0,2.5)),
        Point(Val(4,1), Val(2,2.5)),
        Point(Val(3,1), Val(2,2.5)),
        Point(Val(3,1), Val(3,2.5)),
        Point(Val(1,2), Val(1,3.5)),
        Point(Val(1,0), Val(1,5.5)),
        Point(Val(1,0), Val(1,2)),
        Point(Val(1,-1), Val(1,1)),
        Point(Val(1,-1), Val(1,-1))
    ]

    P = Puzzle(points)
    P.drawPuzzle()
    P.updatePygame()
    sleep(2)

    p = [
        Point(Val(1,0), Val(1,1.5)),
        Point(Val(1,2), Val(1,3.5)),
        Point(Val(1,0), Val(1,5.5))
    ]

    P.addShape(Shape(p))
    P.updatePygame()

    p = [
        Point(Val(1,0), Val(1,1.5)),
        Point(Val(1,1), Val(1,0.5)),
        Point(Val(1,2), Val(1,1.5)),
        Point(Val(1,1), Val(1,2.5))
    ]

    P.addShape(Shape(p))
    P.updatePygame()

    sleep(1)

    P.status = "Solving"
    P.updatePygame()

    solver_rng.placed_pieces = 2
    solver_rng.pieceCount = {
        1:1,
        2:1,
        3:2,
        4:0,
        5:1
    }
    
    solver_rng.solve(copy.deepcopy(P))

    P.status = "Correct"

    sleep(2)

if __name__ == '__main__':
    run_test()
    quit()