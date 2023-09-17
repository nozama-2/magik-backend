from lib import *
import copy
# Use copy.deepcopy to duplicate entire item

def run_test():
    init(plot=False)

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

    p = [
        Point(Val(1,1), Val(1,2.5)),
        Point(Val(2,1), Val(0,2.5)),
        Point(Val(3,1), Val(1,2.5))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(1,-1), Val(1,-1)),
        Point(Val(1,0), Val(1,0)),
        Point(Val(1,0), Val(1,2)),
        Point(Val(1,-1), Val(1,1))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(3,1), Val(1,2.5)),
        Point(Val(3,1), Val(3,2.5)),
        Point(Val(1,1), Val(1,2.5))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(1,0), Val(1,1.5)),
        Point(Val(1,1), Val(1,0.5)),
        Point(Val(1,2), Val(1,1.5)),
        Point(Val(1,1), Val(1,2.5))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(3,1), Val(1,2.5)),
        Point(Val(4,1), Val(2,2.5)),
        Point(Val(3,1), Val(2,2.5))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(1,0), Val(1,1.5)),
        Point(Val(1,2), Val(1,3.5)),
        Point(Val(1,0), Val(1,5.5))
    ]

    P.addShape(Shape(p))

    p = [
        Point(Val(0,0), Val(0,0)),
        Point(Val(1,0), Val(0,0)),
        Point(Val(1,0), Val(1,0))
    ]

    P.addShape(Shape(p))

if __name__ == '__main__':
    run_test()
    quit()