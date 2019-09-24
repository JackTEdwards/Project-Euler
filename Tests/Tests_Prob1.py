import unittest
from Answers import Prob1

class TestsumMul3and5(unittest.TestCase):
    
    def test_sumMul3and5Returns3WhenPassed4(self):
        self.assertEqual(Prob1.sumMul3and5(4), 3)
        
    def test_sumMul3and5Returns8WhenPassed6(self):
        self.assertEqual(Prob1.sumMul3and5(6), 8)

    def test_sumMul3and5Returns23WhenPassed10(self):
        self.assertEqual(Prob1.sumMul3and5(10), 23)

    def test_sumMul3and5Returns233168WhenPassed1000(self):
        self.assertEqual(Prob1.sumMul3and5(1000), 233168)