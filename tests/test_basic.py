from turtletrees import core
import unittest
import random


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
   
        # Checks that changing inp_string is same as running generate function for more iterations
        n = random.randint(1, 6)
        inp_string = core.generate('A+[A]B-', n, 'B+[[A]-A]-B[-BA]+A', 'BA')
        self.assertEqual(core.generate(inp_string, 1, 'B+[[A]-A]-B[-BA]+A', 'BA'),
                         core.generate('A+[A]B-', n+1, 'B+[[A]-A]-B[-BA]+A', 'BA'))

    def test_maxDepth(self):
        """ Tests maxDepth function using tree present output (max_iter=2) """
        self.assertEqual(core.maxDepth('BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A+[BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A]BAB+[[A]-A]-B[-BA]+A-'),
                         5)
