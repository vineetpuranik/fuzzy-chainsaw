import unittest
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # sub-problem in words
        # Let P(i) denote the maximum amount of money the robber can rob from the first i houses without alerting the police


        # base case
        # P(0) = nums(0)
        # P(1) = max(P(0), nums(1))

        # recursion
        # P(i) = max(P(i - 1), nums(i) + P(i - 2))
        # i ranges from 2 to len(nums) - 1
        # either rob the current house which means you can also rob the house that occurs 2 positions before or skip the current house and take the money from the previous house.
       
        if len(nums) == 1: 
            return nums[0]

        result = [0 for _ in range(len(nums))]
        result[0] = nums[0]
        result[1] = max(result[0], nums[1])

        for i in range(2, len(nums)):
            result[i] = max(result[i - 1], (result[i - 2] + nums[i]))

        # Time : O(n)
        # Space : O(n)
        return result[-1]
        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(4, self.solution.rob([1,2,3,1]))

    def test_example_2(self):
        self.assertEqual(12, self.solution.rob([2,7,9,3,1]))
        


if __name__ == '__main__':
    unittest.main()
