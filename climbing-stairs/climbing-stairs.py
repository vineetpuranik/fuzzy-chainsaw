import unittest

class Solution:
    def climbStairs(self, n: int) -> int:
        # create a result array that will include n + 1 elements since we will not be using the element at index 0
        result = [0] * (n + 1)

        # let result[i] correspond to the distinct ways for climbing the first i stairs
        # Base cases
        # result[0] = 0 -> no stairs then 0 ways
        # result[1] = 1 -> 1 stair = 1 way since we can only climb 1 stair and climbing 2 stairs will take us out of bounds.
        # result[2] = 2 -> climb 1 stair from stair 1 or 2 stairs from starting position
        # Recurrence relations
        # we can reach the ith stair from either the i-2 stair by taking 2 steps or from the i-1 stair by taking 1 step.
        # hence result[i] = result[i - 2] + result[i - 1] is our recurrence relation.

        # only 1 stair
        if n == 1:
            return 1

        else: 
            # only 1 stair
            result[1] = 1
            result[2] = 2

            for i in range(3, len(result)):
                result[i] = result[i - 2] + result[i - 1]
            
            return result[n]

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example__1(self):
        self.assertEqual(2, self.solution.climbStairs(2))

    def test_example__2(self):
        self.assertEqual(3, self.solution.climbStairs(3))

    def test_example__3(self):    
        self.assertEqual(5, self.solution.climbStairs(4))

 
            
if __name__ == '__main__':
    unittest.main()
    