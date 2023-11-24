import unittest
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force
        # Check every pair of heights and calculate the area for that pair
        # Area for a pair = height (min height from the pair) * width (distance between the pair)
        # Return the max area from the area of all the pairs. 
        # This takes O(n^2) 
        
        # maxArea  = 0 
        # for l in range(len(height)):
        #    for r in range(1, len(height)):
        #        area = (r - l) *  min(height[i], height[j])
        #        maxArea = max(maxArea, area)
        
        # return maxArea
        
        
        # From the brute force we can see that we need to maximize the area of our container. 
        # So, we will start with 2 pointers l and r. 
        # l : will start from the 1st element
        # r : will start from the last element
        # calculate area for l, r
        # if height[l] > height[r] then , we move shift the right pointer towards l
        # if height[r] > height[l] then, we shift the left pointer towards right
        # this is because we want to maximize the area hence we will keep the pointer which currently has the higher height. 
        # if both heights are equal then we can shift either of the pointers
        
        result = 0
        l, r = 0, len(height) - 1
    
        # iterate while left pointer is less than the right pointer
        while l < r : 
            area = (r - l) * min(height[l], height[r])
            result = max(area, result)
            
            if height[r] > height[l]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                r -= 1
                
        return result

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(49, self.solution.maxArea([1,8,6,2,5,4,8,3,7]))

    def test_example_2(self):
        self.assertEqual(1, self.solution.maxArea([1,1]))


if __name__ == '__main__':
    unittest.main()






