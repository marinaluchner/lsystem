from turtletrees import core
import unittest
from unittest.mock import Mock

class TheoryTest(unittest.TestCase):
    """
    Tests theoretical non-GUI methods of App class
    """
    def test_reproduce(self):
        """ Tests reproduce function using tree preset"""
        self.assertEqual(core.reproduce('A+[A]B-', 'B+[[A]-A]-B[-BA]+A', 'BA'),
                         'B+[[A]-A]-B[-BA]+A+[B+[[A]-A]-B[-BA]+A]BA-')

    def test_generate(self):
        """ Tests generate function using tree preset """
        self.assertEqual(core.generate('A+[A]B-', 2, 'B+[[A]-A]-B[-BA]+A', 'BA'),
                         'BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A+[BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A]BAB+[[A]-A]-B[-BA]+A-')

    def test_maxDepth(self):
        """ Tests maxDepth function using tree present output (max_iter=2) """
        self.assertEqual(core.maxDepth('BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A+[BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A]BAB+[[A]-A]-B[-BA]+A-'),
                         5)
