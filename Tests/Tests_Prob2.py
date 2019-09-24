import unittest
from Answers import Prob2

class TestsumEvenFibonacci(unittest.TestCase):
    
    def test_sumEvenFibonacciReturns10WhenPassed10(self):
        self.assertEqual(Prob2.sumEvenFibonacci(10), 10)

    def test_sumEvenFibonacciReturns13WhenPassed10(self):
        self.assertEqual(Prob2.sumEvenFibonacci(13), 10)

    def test_sumEvenFibonacciReturns4613732WhenPassed4000000(self):
        self.assertEqual(Prob2.sumEvenFibonacci(4000000), 4613732)
        