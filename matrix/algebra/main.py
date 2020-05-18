import csv
import matrix as models
from pprint import pprint
from copy import deepcopy
import itertools
from functools import reduce


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
    ls = read_matrix_with_space('o2') # Для суммы
    matrix = models.Matrix(ls, mod=5)
    b2 = models.Matrix([[x.numerator for x in matrix.columns[4]]], mod=5)
    b1 = models.Matrix([[x.numerator for x in matrix.columns[3]]], mod=5)
    to_step(matrix)

    print(f'b2={b2}, b1={b1}')
    print(f'b2 - b1 = {b2-b1}')

def o2_sup():
    ls = read_matrix_with_space('o2')
    an = [models.Matrix([[x] for x in l], mod=5) for l in ls[:3]]
    bn = [models.Matrix([[x] for x in l], mod=5) for l in ls[3:]]
    cs = [(i, j) for j in range(5) for i in range(5)]
    sums_a = [a * c[0] + b * c[1] for c in cs for a, b in itertools.permutations(an, 2)]
    sums_b = [a * c[0] + b * c[1] for c in cs for a, b in itertools.permutations(bn, 2)]
    ss = {s for s in sums_a if s in sums_b}
    b2b3 = {a * c[0] + b * c[1] for c in cs for a, b in itertools.permutations(bn[1:], 2)}
    print('\n\n'.join(map(str, ss)))
    print(len(ss))
    # print('\n \n'.join(map(str, sums[1])))
    # res = [[' '.join(map(str, sums[i][1])) if l in sums[i][0] else '---' for l in ls] for i in range(len(sums))]
    # pprint(res)
    # print(str(ls[3] + ls[4] * 4))
    # xs = [ls[4] * c[0] + ls[5] * c[1] for c in cs]
    # print('\n \n'.join(map(str, xs)))

def o2_cup():
    ls = read_matrix_with_space('o2')
    an = [models.Matrix([[x] for x in l], mod=5) for l in ls[:3]]
    bn = [models.Matrix([[x] for x in l], mod=5) for l in ls[3:]]
    coefs_2 = [(i, j) for i in range(5) for j in range(5)]
    coefs_3 = [(i, j, k) for i in range(5) for j in range(5) for k in range(5)]
    coefs_4 = [(i, j, k, l) for i in range(5) for j in range(5) for k in range(5) for l in range(5)]
    coefs_5 = [(i, j, k, l, m) for i in range(5) for j in range(5) for k in range(5) for l in range(5) for m in range(5)]
    coefs_6 = [(i, j, k, l, m, n) for i in range(5) for j in range(5) for k in range(5) for l in range(5) for m in range(5) for n in range(5)]
    coefs = {2: coefs_2, 3: coefs_3, 4:coefs_4, 5:coefs_5, 6:coefs_6}

    # ax = []
    # for xs in coefs[len(an)]:
    #     print(len(xs), len(an), '-------')
    #     inits = [z*t for z, t in zip(an, xs)]
    #     r = inits[0] + inits[1]
    #     r = r + inits[2]
    #     ax.append(r)
    xx = lambda an: {reduce(lambda x, y: x+y, [z*t for z, t in zip(an, xs)], 
        models.Matrix([[0] for _ in range(an[0].num_rows)], mod=5))
        for xs in coefs[len(an)]}
    # ax = xx(an)
    # bx = xx(bn)
    # abx = xx([*an, *bn])
    # ss = [a for a in ax if a in bx]
    # print('\n\n'.join(map(str, ss)))
    # print(len(ax))
    # print(len(bx))
    # print(len(ss))
    print(bn[1] in xx([*an[:2], bn[0]]))

def o2_sup():
    ls = read_matrix_with_space('o2')
    an = [models.Matrix([[x] for x in l], mod=5) for l in ls[:3]]
    bn = [models.Matrix([[x] for x in l], mod=5) for l in ls[3:]]
    coefs_2 = [(i, j) for i in range(5) for j in range(5)]
    xs = {bn[0]*b1 + bn[1]*(b1*4) + bn[2]*b3 for b1, b3 in coefs_2}
    print('\n\n'.join(map(str, xs)))
    print(len(xs))
    print(str(bn[0] + bn[1]*4))


def o3():
    M = [models.Matrix(read_matrix_with_space(f'o3_m{i}')) for i in range(1, 5)]
    v = models.Matrix(read_matrix_with_space('o3_v'))
    b2 = models.Matrix(read_matrix_with_space('o3_b2'))
    # A - матрица линейного отображения
    A = models.Matrix([[0]*4 for _ in range(2)])
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
        A.rows[0][i] = x1
        A.rows[1][i] = x2
        print(f'x1={x1}, x2={x2}')
        print('\n')
    # Выводим матрицу отображения
    print(A)
    print(A*models.Matrix([[1], [0], [0], [0]]))

if __name__ == "__main__":
    # o2_sup()
    ls = read_matrix_with_space('spkr')
    matrix = models.Matrix(ls)
    print(matrix)
    matrix.to_step(sorting=False)
