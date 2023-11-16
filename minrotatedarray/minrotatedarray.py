import unittest
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums.length >= 1
        # nums contains all integers that are unique
        # nums is sorted in ascending order and rotated
        # target runtime is O(logn)
        # sorted and O(logn) runtime means we have to use modified binary search


        # if nums contains only a single element then return that element as the answer
        if len(nums) == 1: 
            return nums[0]


        start = 0
        end = len(nums) - 1

        while start < end :
            mid = (start + end) // 2

            if nums[mid] >  nums[end]:
                start = mid + 1
            else: 
                end = mid
                # key is to make sure end is set to mid and not mid - 1 while discarding the right half of the array
                # why because it can happen that our min element will be positioned at mid [3 1 2]. Here mid - 1 will yield a wrong result

        return nums[start]        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_contains_single_element(self):
        self.assertEqual(2, self.solution.findMin([2]))
        
        
    def test_example_1(self):
        self.assertEqual(1, self.solution.findMin([3,4,5,1,2]))


    def test_example_2(self):
        self.assertEqual(0, self.solution.findMin([4,5,6,7,0,1,2]))


    def test_example_3(self):
        self.assertEqual(11, self.solution.findMin([11,13,15,17]))


if __name__ == '__main__':
    unittest.main()


