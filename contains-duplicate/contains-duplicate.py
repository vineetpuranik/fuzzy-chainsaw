from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Given an integer array nums, return true if any value appears at least twice in the array, 
        # and return false if every element is distinct.
        # at least 1 element in the array based on the constraints

        # if there is only 1 element
        if len(nums) == 1 : 
            return False

        numsSet = set()

        for i in range(len(nums)):
            if nums[i] in numsSet:
                return True    

            numsSet.add(nums[i])

        # if we reach here that means there is no duplicate
        return False    


# space complexity : O(n)
# time complexity : O(n)