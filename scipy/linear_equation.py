import numpy


def solve(A, b):
    try:
        print(numpy.linalg.solve(A, b))
    except numpy.linalg.LinAlgError:
        raise RuntimeError('det(A) = 0!!')

def one():
    A = [
            [0,1,2,3,4],
            [2,3,9,0,0],
            [0,0,0,3,0],
            [777,239,0,0,0],
            [7,0,7,0,7],
            ]
    b = [30,21,9,239,42]
    solve(A, b)

def two():
    A = [
            [0,1,2,3,4],
            [2,3,9,0,0],
            [0,2,4,6,8],
            [777,239,0,0,0],
            [7,0,7,0,7],
            ]
    b = [30,21,9,239,42]
    solve(A, b)

one()
two()
