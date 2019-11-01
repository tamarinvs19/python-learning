import logging as log
from matrix import Number, Matrix, get_k_to_b, count_start_zero


def test_matrix():
    a = Matrix([[1, 2, 0],[0, 1, 3]])
    b = Matrix([[1, 1, 1], [1, 0, 0], [2, 2, 1]])

    assert a.num_columns == 3
    assert b.num_columns == 3
    assert a.num_rows == 2
    assert b.num_rows == 3
    assert a.order == (2, 3)
    assert b.order == (3, 3)
    assert a.is_square == False
    assert b.is_square == True
    assert a.columns == [[1, 0], [2, 1], [0, 3]]
    assert b.columns == [[1, 1, 2], [1, 0, 2], [1, 0, 1]]
    assert a.identity_columns() == Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert b.identity_columns() == Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert a.identity_rows() == Matrix([[1, 0], [0, 1]])
    a.transpose()
    assert a == Matrix([[1, 0], [2, 1], [0, 3]])
    a.transpose()

    assert a * b == Matrix([[3, 1, 1], [7, 6, 3]])
    assert a * 2 == Matrix([[2, 4, 0], [0, 2, 6]])

    assert (a==b) == False
    assert a != b
    assert - a == Matrix([[-1, -2, 0], [0, -1, -3]])

    c = Matrix([[1, 2, 0],[0, 1, 3]])

    assert a + c == Matrix([[2, 4, 0], [0, 2, 6]])
    assert a - c == Matrix([[0, 0, 0], [0, 0, 0]])

    c.add_row([0, 1, 1])
    assert c.rows[-1] == [0, 1, 1]
    c.add_column([0, 1, 2])
    assert c.columns[-1] == [0, 1, 2]

    c.add_row([0, 0, 2, 6], 1)
    c.sort_by_zero()
    assert c == Matrix([[1, 2, 0, 0], [0, 1, 3, 1], [0, 1, 1, 2], [0, 0, 2, 6]])

    c.to_one_in_first_no_zero(3)
    assert c.rows[3] == [0, 0, 1, 3]

    log.info(b.__str__())
    b.elementary_transformation(0, 2, 0)
    log.info(b.__str__())
    assert b.rows[2] == [0, 0, -1]

    d = Matrix([[0, 0, 1, 0], [0, 0, 2, 0]], mod=5)
    d.elementary_transformation(0, 1, 2)
    assert d.rows[1] == [0, 0, 0, 0]

def test_get_k():
    assert get_k_to_b(1, 2, 3) == 1
    assert get_k_to_b(4, 1, 8) == 4
    assert get_k_to_b(4, 1, 0, module=7) == 3

def test_cout_start_zero():
    assert count_start_zero([0, 0, 1, 0, 4]) == 2
    assert count_start_zero([0, 0, 0, 0, 4]) == 4
    assert count_start_zero([2, 0, 1, 0, 4]) == 0

def test_number_module_7():
    global module
    module = 7
    a = Number(2)
    b = Number(10)
    assert Number(-2).numerator == Number(5).numerator
    assert Number(3) == 3
    assert -a    == Number(5)
    assert -b    == Number(4)
    assert a * b == Number(6)
    assert a + b == Number(5)
    assert a - b == Number(6)
    assert a * 2 == Number(4)
    assert b + 3 == Number(6)

    assert Number(2) == Number(2)
    assert Number(2) != Number(3)
    assert b > 1
    assert b > a
    assert b < 6
    assert a < b
    assert b == 3
    assert a == 2
    assert a != 239

    assert abs(a) == 2
    assert divmod(a, b) == (0, 2)
    assert divmod(a, 4) == (0, 2)
    assert divmod(9, b) == (3, 0)
    assert a % b  == 2
    assert b // a == 1
