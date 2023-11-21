import unittest
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int: 
        # use 2 pointers
        # l for buying and r for selling
        # buy low and sell high

        l, r = 0, 1
        maxP = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)

            else: # value at l pointer is greater than value at right pointer so, we move the left pointer
                l = r

            r +=  1 # r is incremeted in every iteration of the while loop.


        return maxP




class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(5, self.solution.maxProfit([7,1,5,3,6,4]))


    def test_example_2(self):    
        self.assertEqual(0, self.solution.maxProfit([7,6,4,3,1]))


if __name__ == '__main__':
    unittest.main()

