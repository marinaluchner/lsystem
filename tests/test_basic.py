from turtletrees import core
from turtletrees.core import App
import unittest
import random
import tkinter as tk


class TheoryTest(unittest.TestCase):
    """
    Tests L-system functions
    """
    def test_reproduce(self):
        """ Tests reproduce function using tree preset"""
        self.assertEqual(core.reproduce('A+[A]B-', 'B+[[A]-A]-B[-BA]+A', 'BA'),
                         'B+[[A]-A]-B[-BA]+A+[B+[[A]-A]-B[-BA]+A]BA-')

    def test_generate(self):
        """ Tests generate function using tree preset """
        self.assertEqual(core.generate('A+[A]B-', 2, 'B+[[A]-A]-B[-BA]+A', 'BA'),
                         'BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A+[BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A]BAB+[[A]-A]-B[-BA]+A-')
   
        # Checks that running for n+1 iterations is same as running once on the output of n iterations
        n = random.randint(1, 6)
        inp_string = core.generate('A+[A]B-', n, 'B+[[A]-A]-B[-BA]+A', 'BA')
        self.assertEqual(core.generate(inp_string, 1, 'B+[[A]-A]-B[-BA]+A', 'BA'),
                         core.generate('A+[A]B-', n+1, 'B+[[A]-A]-B[-BA]+A', 'BA'))

    def test_maxDepth(self):
        """ Tests maxDepth function using tree present output (max_iter=2) """
        self.assertEqual(core.maxDepth('BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A+[BA+[[B+[[A]-A]-B[-BA]+A]-B+[[A]-A]-B[-BA]+A]-BA[-BAB+[[A]-A]-B[-BA]+A]+B+[[A]-A]-B[-BA]+A]BAB+[[A]-A]-B[-BA]+A-'),
                         5)

class AppTest(unittest.TestCase):
    
    def test_create(self):
        root = tk.Tk()
        app = App(root)