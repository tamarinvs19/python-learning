import unittest
from unittest import patch, MagicMock
from models import Wolf, Rabbit
import cmath


class TestWolf(unittest.TestCase):
    def test_init(self):
        c = complex(1, 1)
        v = complex(1, 1)
        wolf = Wolf(c, v)
        self.assertEqual(wolf.c, c)
        self.assertEqual(wolf.v, v)

    @patch('wolf.v', side_effect=[complex(1, 1), complex(-1, -1), complex(2, -1)])
    def test_move(self, m_v):
        wolf = Wolf(complex(1, 1))
        wolf.move()
        self.assertEqual(wolf.c, complex(2, 2))
        wolf.move()
        self.assertEqual(wolf.c, complex(1, 1))
        wolf.move()
        self.assertEqual(wolf.c, complex(3, 0))
    
    def test_radar(self):

