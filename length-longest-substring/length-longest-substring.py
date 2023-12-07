import unittest
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 : 
            return 0
        result = 0
        left = 0
        charSet = set()

        for right in range(len(s)):
            #if current character is in the set
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, (right - left + 1))            

        return result    


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(3, self.solution.lengthOfLongestSubstring('abcabcbb'))    

    def test_example_2(self):
        self.assertEqual(3, self.solution.lengthOfLongestSubstring('pwwkew'))    

    def test_example_3(self):
        self.assertEqual(1, self.solution.lengthOfLongestSubstring('bbbbbb'))    


if __name__ == '__main__':
    unittest.main()