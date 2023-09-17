from lib import *
import copy
# Use copy.deepcopy to duplicate entire item

def run_test():
    init(plot=False)

    points = [
        Point(Val(1,0), Val(0,0)),
        Point(Val(0,0), Val(1,0)),
        Point(Val(1,0), Val(1,0)),
        Point(Val(1,0), Val(3,0)),
        Point(Val(2,0), Val(4,0)),
        Point(Val(2,0), Val(3,0)),
        Point(Val(4,0), Val(3,0)),
        Point(Val(4,2), Val(3,-2)),
        Point(Val(4,2), Val(2,-2)),
        Point(Val(3,2), Val(3,-2)),
        Point(Val(4,-2), Val(3,-2))
    ]

    P = Puzzle(points)
    P.drawPuzzle()
    print(P)

    p = [
        Point(Val(4,0), Val(3,0)),
        Point(Val(4,2), Val(3,-2)),
        Point(Val(4,-2), Val(3,-2))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(4,2), Val(3,-2)),
        Point(Val(4,2), Val(2,-2)),
        Point(Val(3,2), Val(3,-2))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(4,0), Val(3,0)),
        Point(Val(2,0), Val(1,0)),
        Point(Val(2,0), Val(3,0))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(1,0), Val(3,0)),
        Point(Val(2,0), Val(4,0)),
        Point(Val(2,0), Val(3,0)),
        Point(Val(1,0), Val(2,0))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(1,0), Val(2,0)),
        Point(Val(2,0), Val(2,0)),
        Point(Val(2,0), Val(3,0))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(1,0), Val(0,0)),
        Point(Val(0,0), Val(1,0)),
        Point(Val(2,0), Val(1,0))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(1,0), Val(1,0)),
        Point(Val(2,0), Val(1,0)),
        Point(Val(2,0), Val(2,0)),
        Point(Val(1,0), Val(2,0))
    ]

    P.addShape(Shape(p))

    print(P)

    quit()
