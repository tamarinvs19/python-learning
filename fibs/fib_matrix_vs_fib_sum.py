def pow(x, n, I, mult):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y

def identity_matrix(n):
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]

def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]

def fib_matrix(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]

def fib_sum(n):
    a = 1
    b = 1
    for _ in range(3, n):
        a, b = b, a+b
    return b

import timeit
print(timeit.timeit('fib_sum(10**8)', number=1, globals={'fib_sum':fib_sum}))
print(timeit.timeit('fib_matrix(10**8)', number=1, globals={'fib_matrix':fib_matrix}))
