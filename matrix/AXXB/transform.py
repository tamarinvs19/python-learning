import numpy as np
from pprint import pprint


def transform(name):
    size = 4
    a = [[0]*size for _ in range(size)]
    a[0][0] = 1
    a[1][1] = 1
    a[2][2] = (1-1j)/(2**0.5)
    a[3][3] = (1+1j)/(2**0.5)
    # with open(name, 'r') as f:
    #     for i in range(4):
    #         a.append(list(map(int, f.readline().split())))
    # pprint(a)
    t = 1/2**0.5
    b = [[0]*size for i in range(size)]
    b[0][0] = 1
    b[1][1] = -1
    b[2][2] = t
    b[2][3] = -t
    b[3][2] = t
    b[3][3] = t

    at = [[0] * size**2 for _ in range(size**2)]
    for i in range(size):
        for j in range(size):
            for x in range(size):
                for y in range(size):
                    at[i*size+x][j*size+y] = a[i][j] if x == y else 0
    at = np.array(at)
    bt = [[0] * size**2 for _ in range(size**2)]
    bm = np.array(b)
    bt = np.concatenate(
            [np.concatenate([bm.T if i == j else np.zeros((4, 4)) for j in range(size)]) for i in range(size)], axis=1)
    # pprint(at)
    # pprint(bt)
    q = at + bt
    pprint(q.shape)
    pprint(np.linalg.solve(q, np.array([0]*size**2)))

if __name__ == '__main__':
    transform('matr')
