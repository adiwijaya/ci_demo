"""
Unit tests for the calculator library
# python -m unittest test_calculator.py -v
"""
#test

import calculator
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(4, calculator.add(2, 2))

    def test_subtraction(self):
        self.assertEqual(2, calculator.subtract(4, 2))

if __name__ == '__main__':
    """
    Verbosity level
    0 (quiet): you just get the total numbers of tests executed and the global result
    1 (default): you get the same plus a dot for every successful test or a F for every failure
    2 (verbose): you get the help string of every test and the result
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)
