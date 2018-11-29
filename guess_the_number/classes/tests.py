import unittest
from unittest.mock import patch, MagicMock
from guesser import ComputerRiddler, HumanGuesser

class TestComputerRiddler(unittest.TestCase):
    def test_correct_initializatin(self):
        cr = ComputerRiddler()
        self.assertIn('number', cr.__dict__) # появляется ли число при создании cr
        self.assertTrue(hasattr(cr, 'number') and type(cr.number) == int) # есть ли объект 'number' в cr и целое ли это число
        self.assertTrue(1 <= cr.number <= 99) # проверка значения

    @patch('guesser.ComputerRiddler')
    def test_check(self, m_CR):
        #cr = ComputerRiddler()
        cr = MagicMock(spec=ComputerRiddler)
        cr.check = ComputerRiddler.check
        cr.number = 50
        self.assertEqual((True, '='), cr.check(50)) # тест на равенство двух значений
        self.assertEqual((False, '>'), cr.check(25))
        self.assertEqual((False, '<'), cr.check(75))


class TestHumanGuesser(unittest.TestCase):
    '''
    @patch('guesser.input', return_value='16') # меняем input в файле guesser только на выполнение этого теста, теперь при вызове здесь input() возвращает 16
    '''
    @patch('guesser.input', side_effect=['16', '16.5']) # в первый раз будет выдавать 16, потом 16.5
    def test_guess(self, m_input): # m_input - объект класса MagicMock
        hg = HumanGuesser()
        self.assertEqual(16, hg.guess())
        m_input.assert_called_with('Предположите: ')
        #print(m_input.call_args_list) # просмотр вызовов m_input
        with self.assertRaises(ValueError):
            hg.guess()
        
 

if __name__ == '__main__':
    unittest.main()
