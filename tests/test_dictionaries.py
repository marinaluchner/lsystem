from turtletrees import core
from turtletrees.core import App
import unittest


from unittest.mock import Mock
stack = Mock(return_value=[((71.20,-139.20), 70.0)])
stack_depth = Mock(return_value = 1)

def test_change_pen_color(self):
    """ Test change_pen_color function using tree preset"""
    self.assertEqual(core.App.change_pen_color(stack, stack_depth, start_color = (0.6, 0.3, 0), final_color = (0.4, 1, 0.4)), [0.5, 0.6499999999999999, 0.2])
    