import csv
import matrix as models
from pprint import pprint
from copy import deepcopy


def read_matrix_with_space(name):
    with open(name, 'r') as f:
        lines = [list(map(int, line.split())) for line in f.readlines()]
    return lines

def to_step(matrix):
    print(matrix)
    matrix.to_step()

def o1():
    ls = read_matrix_with_space('o1')
    matrix = models.Matrix(ls, mod=7)
    to_step(matrix)

def o2():
    ls = read_matrix_with_space('base1') # Для суммы
    matrix = models.Matrix(ls, mod=5)
    to_step(matrix)

def o3():
    M = [models.Matrix(read_matrix_with_space(f'o3_m{i}')) for i in range(1, 5)]
    v = models.Matrix(read_matrix_with_space('o3_v'))
    b2 = models.Matrix(read_matrix_with_space('o3_b2'))
    # A - матрица линейного отображения
    A = [[0]*4 for _ in range(2)]
    for i, m in enumerate(M):
        p = m*v # умножаем один из базисных векторов M на v
        b = deepcopy(b2)
        b.add_column(p.columns[0]) # добавляем полученный вектор к базису в Q^2 как третий столбец
        print('b=', b, sep='\n')
        b.to_step() # методом Гаусса приводим к ступеньчатому виду
        # Выражаем p через базис в Q^2 (считаем координаты)
        x2 = b.rows[1][2]
        x1 = - b.rows[0][1] * x2 + b.rows[0][2]
        # И записываем координаты в матрицу отображения
        A[0][i] = x1
        A[1][i] = x2
        print(f'x1={x1}, x2={x2}')
        print('\n')
    # Выводим матрицу отображения
    pprint([[str(x) for x in a] for a in A])

if __name__ == "__main__":
    o3()
