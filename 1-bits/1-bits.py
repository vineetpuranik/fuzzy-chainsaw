import unittest
from typing import List

class Solution:
    def hammingWeight(self, n : int) -> int:
        #we will always have an input

        result = 0
        #idea : check lsb is 0 or 1 and then right shift n

        while n > 0: 
            if n % 2 > 0: 
                result += 1

            n = n >> 1    

        return result
        # O(32) : since at most we have to check all the 32 bits. This is constant and hence the overall time complexity is O(1)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):
        self.assertEqual(3, self.solution.hammingWeight(11))


if __name__ == '__main__':
    unittest.main()