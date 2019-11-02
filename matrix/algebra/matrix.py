import pdb
import logging as log
from pprint import pprint
from fractions import Fraction


global module

def reverse_matrix(matrix):
    rows = [[e.numerator for e in row] for row in matrix.rows]
    rk = len(rows) - rows.count([0] * len(rows[0]))
    last_row = rows[rk-1]
    last_row.reverse()
    last_index_of_one = len(last_row) - last_row.index(1) - 1
    last_row.reverse()
    rows.reverse()
    new_rows = [reverse_list(row[:last_index_of_one+1]) + row[last_index_of_one+1:] for row in rows]
    return new_rows

def reverse_list(ls):
    ls = [ls[-i] for i in range(1, len(ls)+1)]
    return ls

def get_k_to_b(k, first, b, module=0):
    if module == 0:
        return Fraction(b - k, first)
    else:
        for i in range(0, module):
            if (k + first * i) % module == b:
                return i

def f(invert, row, i):
    if invert: return i > -1
    else: return i < row -1

def count_start_zero(row, invert=False):
    if invert: i = len(row) -1
    else: i = 0
    while row[i] == 0 and f(invert, len(row), i):
        if invert: i -= 1
        else: i += 1
    return i

class Number:
    def __init__(self, numerator):
        global module
        self.module = module
        self.numerator = pow(numerator, 1, self.module)

    def __add__(self, x):
        new_numerator = self.numerator + x.numerator
        global module
        module = self.module
        return Number(new_numerator)

    def __radd__(self, x):
        new_numerator = x.numerator + self.numerator
        return Number(new_numerator)

    def __rsub__(self, x):
        new_numerator = x.numerator - self.numerator
        return Number(new_numerator)

    def __sub__(self, x):
        new_numerator = self.numerator - x.numerator
        return Number(new_numerator)

    def __rmul__(self, x):
        new_numerator = x.numerator * self.numerator
        return Number(new_numerator)

    def __mul__(self, x):
        new_numerator = self.numerator * x.numerator
        return Number(new_numerator)
    
    def __neg__(self):
        return self.module - self.numerator

    def __eq__(self, value):
        return self.numerator == value

    def __ne(self, value):
        return self.numerator != value

    def __le__(self, x):
        return self.numerator <= pow(x.numerator, 1, self.module)

    def __lt__(self, x):
        return self.numerator < pow(x.numerator, 1, self.module)

    def __ge__(self, x):
        return self.numerator >= pow(x.numerator, 1, self.module)

    def __gt__(self, x):
        return self.numerator > pow(x.numerator, 1, self.module)

    def __abs__(self):
        return abs(self.numerator)

    def __ceil__(self):
        return self.numerator

    def __rdivmod__(self, x):
        return divmod(x.numerator, self.numerator)

    def __divmod__(self, x):
        return divmod(self.numerator, x.numerator)

    def __rfloordiv__(self, x):
        return x.numerator // self.numerator

    def __floordiv__(self, x):
        return self.numerator // x.numerator

    def __rmod__(self, x):
        return x.numerator % self.numerator

    def __mod__(self, x):
        return self.numerator % x.numerator

    def __hash__(self):
        return hash(self.numerator)

    def __int__(self):
        return self.numerator

    def __str__(self):
        return str(self.numerator)

class Matrix:
    def __init__(self, rows, mod=0):
        global module
        module = mod
        if mod:
            self.rows = [[Number(e) for e in line] for line in rows]
        else:
            self.rows = rows
        self.module = mod

    @property
    def num_rows(self):
        return len(self.rows)

    @property
    def num_columns(self):
        return len(self.rows[0])

    @property
    def order(self):
        return (len(self.rows), len(self.rows[0]))

    @property
    def is_square(self):
        return self.order[0] == self.order[1]

    @property
    def columns(self):
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    def identity_rows(self, k=1):
        values = [
            [0 if column_num != row_num else k for column_num in range(self.num_rows)]
            for row_num in range(self.num_rows)
        ]
        return Matrix(values, self.module)

    def identity_columns(self, k=1):
        values = [
            [0 if column_num != row_num else k for column_num in range(self.num_columns)]
            for row_num in range(self.num_columns)
        ]
        return Matrix(values, self.module)

    def __repr__(self):
        return str(self.rows)

    def __str__(self):
        return '\n'.join(
                        map(lambda row: '|' + ' '.join(map(str, row)) + '|', 
                        self.rows))

    def __mul__(self, b):
        m, n = self.order
        if isinstance(b, int) or isinstance(b, Number):
            b = self.identity_columns(b)
        o, p = b.order
        assert o == n

        matrix = Matrix([[0] * p for _ in range(m)], mod=self.module)
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    matrix.rows[i][j] += self.rows[i][k] * b.rows[k][j]
        return matrix

    def add_row(self, row, position=None):
        if position is None:
            self.rows.append(row)
        else:
            self.rows = self.rows[0:position] + [row] + self.rows[position:]

    def add_column(self, column, position=None):
        if position is None:
            self.rows = [self.rows[i] + [column[i]] for i in range(self.num_rows)]
        else:
            self.rows = [
                self.rows[i][0:position] + [column[i]] + self.rows[i][position:]
                for i in range(self.num_rows)
            ]

    def transpose(self):
        print('--- transpose ---')
        self.rows = self.columns
        print(self)
        print(' --- end transpose --- ')

    def sort_by_zero(self, reverse=False, invert=False):
        count_zero = [(count_start_zero(row, invert=invert), row) for row in self.rows]
        count_zero.sort(key=(lambda x: x[0]), reverse=reverse)
        self.rows = [count[1] for count in count_zero]

    def elementary_transformation(self, a, b, ind):
        if type(self.rows[a][ind]) == float or type(self.rows[b][ind]) == float:
            x = get_k_to_b(self.rows[b][ind], self.rows[a][ind], 0, module=self.module)
        else:
            x = get_k_to_b(self.rows[b][ind].numerator, self.rows[a][ind].numerator, 0, module=self.module)
        self.rows[b] = [k * x + l for k, l in zip(self.rows[a], self.rows[b])]

    def to_one_in_first_no_zero(self, number_row):
        ind = count_start_zero(self.rows[number_row])
        if type(self.rows[number_row][ind]) == float:
            first_element = self.rows[number_row][ind]
        else:
            first_element = self.rows[number_row][ind].numerator
        x = get_k_to_b(0, first_element, 1, module=self.module)
        self.rows[number_row] = [e*x for e in self.rows[number_row]]
    
    def to_step(self, sorting=True):
        print('---- start  to_step ----')
        ind = 0
        for a in range(len(self.rows)):
            print(' -- -- -- ')
            if sorting:
                while ind < self.num_columns and self.rows[a][ind] == 0:
                    self.sort_by_zero()
                    if self.rows[a][ind] == 0: ind += 1
            if ind < self.num_columns:
                if self.rows[a][ind] != 0:
                    self.to_one_in_first_no_zero(a)
                    for b in range(a+1, len(self.rows)):
                        self.elementary_transformation(a, b, ind)
                    print(self)
                    ind += 1

    def to_step_overhand(self):
        print('---- start to_step_overhand ----')
        new_rows = reverse_matrix(self)
        m1 = Matrix(new_rows, mod=self.module) 
        m1.sort_by_zero()
        print(m1)
        m1.to_step()
        new_rows = reverse_matrix(m1)
        self.rows = new_rows
        
        print('---- end to_step_overhand ----')

    def __eq__(self, other):
        return self.rows == other.rows

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return self * -1

    def __add__(self, other):
        return Matrix(
            [
                [self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __hash__(self):
        return hash(str(self))

    def __sub__(self, other):
        return Matrix(
            [
                [self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

