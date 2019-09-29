import unittest
from Answers import Prob4

class TestisPalindrome(unittest.TestCase):
    
    def test_isPalindromeReturnsTrueWhenPassed11(self):
        self.assertEqual(Prob4.isPalindrome(11), True)

    def test_isPalindromeReturnsFalseWhenPassed12(self):
        self.assertEqual(Prob4.isPalindrome(12), False)

    def test_isPalindromeReturnsTrueWhenPassed101(self):
        self.assertEqual(Prob4.isPalindrome(101), True)
    
    def test_isPalindromeReturnsFalseWhenPassed102(self):
        self.assertEqual(Prob4.isPalindrome(1012), False)

    def test_findLargestPalindromeReturns9009WhenPassed2(self):
        self.assertEqual(Prob4.findLargestPalindrome(2), 9009)