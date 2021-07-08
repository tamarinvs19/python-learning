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

def fib(n):
    F = pow([[1, 1], [1, 0]], n-1, identity_matrix(2), matrix_multiply)
    return F[0][0], F[0][1], F[1][1]
# c, b, a = fib(20182018)
# res = 0
# phi = (1+5**0.5)/2
# for n in range(20182019, 20192019):
#     a, b, c = b, a+b, b+b+a
#     if (c%2 + a%2)%2 == 0:
#         res += 1
# print(res)
print(fib(100) % 10)
