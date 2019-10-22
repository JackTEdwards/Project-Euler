import unittest
from Answers import Prob5

class TestsmallestDivisible(unittest.TestCase):

    def test_smallestDivisibleReturns2520When10Passed(self):
        self.assertEqual(Prob5.smallestDivisible(10), 2520)

    def test_smallestDivisableReturns232792560When20Passed(self):
        self.assertEqual(Prob5.smallestDivisible(20), 232792560)
