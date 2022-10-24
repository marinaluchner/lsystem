# -*- coding: utf-8 -*-

from .context import turtletrees

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(turtletrees.hmm())


if __name__ == '__main__':
    unittest.main()
