import unittest
from Answers import Prob3

class TestgetLargestPrimeFactor(unittest.TestCase):
    
    def test_getLargestPrimeFactorReturns2WhenPassed2(self):
        self.assertEqual(Prob3.getLargestPrimeFactor(10), 5)

    def test_getLargestPrimeFactorReturns5WhenPassed10(self):
        self.assertEqual(Prob3.getLargestPrimeFactor(10), 5)

    def test_getLargestPrimeFactorReturns6857WhenPassed600851475143(self):
        self.assertEqual(Prob3.getLargestPrimeFactor(600851475143), 6857)