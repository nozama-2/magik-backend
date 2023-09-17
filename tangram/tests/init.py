from lib import *

def run_test():
    init(plot=False)

    A = Point(Val(0,0), Val(0,0))
    B = Point(Val(0,4), Val(0,0))
    C = Point(Val(0,4), Val(0,4))
    D = Point(Val(0,0), Val(0,4))
    P = Puzzle([A,B,C,D])
    P.drawPuzzle()
    print("Area: ",P.shape.area())
    print(P)

    A = Point(Val(0,2), Val(0,2))
    B = Point(Val(0,0), Val(0,4))
    C = Point(Val(0,0), Val(0,0))
    T = Shape([A,B,C])
    T.drawShape()

    A = Point(Val(0,2), Val(0,2))
    B = Point(Val(0,4), Val(0,0))
    C = Point(Val(0,0), Val(0,0))
    T = Shape([A,B,C])
    T.drawShape()

    A = Point(Val(0,4), Val(0,0))
    B = Point(Val(0,3), Val(0,1))
    C = Point(Val(0,3), Val(0,3))
    D = Point(Val(0,4), Val(0,2))
    T = Shape([A,B,C,D])
    T.drawShape()

    main()