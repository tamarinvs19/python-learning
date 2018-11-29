import unittest
from guesser import ComputerRiddler

class TestComputerRiddler(unittest.TestCase):
    def test_correct_initializatin(self):
        cr = ComputerRiddler()
        self.assertIn('number', cr.__dict__) # появляется ли число при создании cr
        self.assertTrue(hasattr(cr, 'number') and type(cr.number) == int) # есть ли объект 'number' в cr и целое ли это число
        self.assertTrue(1 <= cr.number <= 99) # проверка значения

    def test_check(self):
        cr = ComputerRiddler()
        cr.number = 50
        self.assertEqual((True, '='), cr.check(50)) # тест на равенство двух значений
        self.assertEqual((False, '>'), cr.check(25))
        self.assertEqual((False, '<'), cr.check(75))
        

if __name__ == '__main__':
    unittest.main()
