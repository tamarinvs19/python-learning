import pdb
from pprint import pprint
global_module = 7

def get_k_to_b(k, first, b):
    for i in range(1, 8):
        if (k + first * i) % global_module == b:
            return i

class Number(int):
    module = global_module
    def __init__(self, value):
        self.value = value

    def __add__(self, x):
        return Number((self.value + x) % self.module)

    def __mul__(self, x):
        return Number((self.value * x) % self.module)

class LineMatrix():
    def __init__(self, xs):
        self.elements = [Number(x) for x in xs]

    @property
    def count_start_zero(self):
        i = 0
        while self.elements[i] == 0 and i < len(self.elements) - 1:
            i += 1
        return i

    def __len__(self):
        return len(self.elements)

    def __add__(self, other_line):
        assert len(other_line) == len(self.elements)
        return LineMatrix([a + b for a, b in zip(self.elements, other_line.elements)])

    def __mul__(self, alpha):
        return LineMatrix([x * alpha for x in self.elements])

    def __iter__(self):
        iter(self.elements)

    def __str__(self):
        return self.elements

class Matrix:
    def __init__(self, lines):
        self.lines = [LineMatrix(line) for line in lines]

    def sort_by_zero(self, reverse=False):
        count_zero = [(line.count_start_zero, line) for line in self.lines]
        count_zero.sort(key=(lambda x: x[0]), reverse=reverse)
        self.lines = [count[1] for count in count_zero]

    def similar_change(self, a, b, ind):
        x = get_k_to_b(self.lines[b].elements[ind].value, self.lines[a].elements[ind].value, 0)
        self.lines[b] = self.lines[b] + self.lines[a] * x

    def to_one_in_first_no_zero(self, number_line):
        ind = self.lines[number_line].count_start_zero
        first_element = self.lines[number_line].elements[ind].value
        x = get_k_to_b(0, first_element, 1)
        self.lines[number_line] = self.lines[number_line] * x
    
    def to_step(self):
        print('---- start ----')
        for a in range(len(self.lines)):
            print(' -- -- -- ')
            self.to_one_in_first_no_zero(a)
            for b in range(a+1, len(self.lines)):
                self.similar_change(a, b, a)
            print(self)

    def __add__(self, matrix):
        return Matrix([a + b for a, b in zip(self.lines, matrix)])

    def __mul__(self, alpha):
        return Matrix([(line * alpha).elements for line in self.lines])

    def __str__(self):
        return '\n'.join(map(lambda x: ' '.join(map(str, x.__str__())), self.lines))
        # return [line.__str__() for line in self.lines]

