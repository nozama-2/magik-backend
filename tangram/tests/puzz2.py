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

    p = [
        Point(Val(0,2), Val(0,4)),
        Point(Val(0,1), Val(0,3)),
        Point(Val(0,2), Val(0,2)),
        Point(Val(0,3), Val(0,3))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(0,4), Val(0,4)),
        Point(Val(0,2), Val(0,4)),
        Point(Val(0,4), Val(0,2))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(0,0), Val(0,0)),
        Point(Val(0,0), Val(0,4)),
        Point(Val(0,2), Val(0,2))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(0,2), Val(0,2)),
        Point(Val(0,3), Val(0,3)),
        Point(Val(0,3), Val(0,1))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(0,1), Val(0,3)),
        Point(Val(0,0), Val(0,4)),
        Point(Val(0,2), Val(0,4))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(0,0), Val(0,0)),
        Point(Val(0,4), Val(0,0)),
        Point(Val(0,2), Val(0,2))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(0,3), Val(0,3)),
        Point(Val(0,3), Val(0,1)),
        Point(Val(0,4), Val(0,0)),
        Point(Val(0,4), Val(0,2))
    ]

    P.addShape(Shape(p))

if __name__ == '__main__':
    run_test()
    quit()
