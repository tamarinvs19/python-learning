import numpy as np


def find_matrix(n):
    for _ in range(n):
        m = np.random.randint(0, 2, (1, 121)).reshape(-1)
        for i, v in enumerate(m):
            if v == 0:
                m[i] = -1
        m = m.reshape(11, 11)

        if np.linalg.det(m) > 4000:
            print(m, np.linalg.det(m))
            break


if __name__ == '__main__':
    find_matrix(10**7)
