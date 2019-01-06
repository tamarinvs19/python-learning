import unittest
from unittest.mock import patch, MagicMock
from guesser import ComputerRiddler, HumanGuesser, ComputerRiddlerHard

class TestComputerRiddler(unittest.TestCase):
    def test_correct_initializatin(self):
        cr = ComputerRiddler()
        self.assertIn('number', cr.__dict__) # появляется ли число при создании cr
        self.assertTrue(hasattr(cr, 'number') and type(cr.number) == int) # есть ли объект 'number' в cr и целое ли это число
        self.assertTrue(1 <= cr.number <= 99) # проверка значения

    #@patch('guesser.ComputerRiddler')
    def test_check(self):  #  , m_CR):
        cr = ComputerRiddler()
        #cr = MagicMock(spec=ComputerRiddler)
        #cr.check = ComputerRiddler.check
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


class TestComputerRiddlerHard(unittest.TestCase):
    def test_correct_initializatin(self):
        crh = ComputerRiddlerHard()
        self.assertIn('borders', crh.__dict__)
        self.assertTrue(hasattr(crh, 'borders') and type(crh.borders) == dict)
        self.assertTrue(crh.borders['left'] == 1 and crh.borders['right'] == 100)
    
    @patch('guesser.ComputerRiddlerHard')
    def test_check_start(self, m_crh):
        crh = MagicMock(spec=ComputerRiddlerHard)
        crh.check = ComputerRiddlerHard.check
        print(crh.check)
        self.assertEqual((False, '>'), crh.check(25))
        print(crh.borders)
        self.assertEqual((False, '>'), crh.check(49))
        self.assertEqual((False, '<'), crh.check(75))
        self.assertEqual((False, '<'), crh.check(51))
        self.assertEqual((False, '>'), crh.check(50))
        self.assertEqual((False, '<'), crh.check(100))
        self.assertEqual((False, '>'), crh.check(1))

    def test_check_in_game(self):
        crh = ComputerRiddlerHard()
        crh.borders['left'], crh.borders['right'] = 10, 25
        self.assertEqual((False, '<'), crh.check(25))
        self.assertEqual((False, '<'), crh.check(49))
        self.assertEqual((False, '>'), crh.check(9))
        self.assertEqual((False, '>'), crh.check(15))
        self.assertEqual((False, '>'), crh.check(10))

    def test_check_finish(self):
        crh = ComputerRiddlerHard()
        crh.borders['left'], crh.borders['right'] = 25, 25
        self.assertEqual((True, '='), crh.check(25))
        self.assertEqual((False, '<'), crh.check(100))
        self.assertEqual((False, '>'), crh.check(9))




if __name__ == '__main__':
    unittest.main()
