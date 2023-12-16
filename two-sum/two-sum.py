class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # an answer will always exist
        # len(nums) is atleast 2 
        # target can be negative and nums[i] can also be negative
        # same element cannot be used twice
        # every input will have exactly 1 unique solution
        # we have to return the 2 unique indices that sum up to the target
        
        # brute force: 
        # for each pair of indices check if the values sum up to the target sum
        # O(n^2) solution
        
        # linear time solution
        # a + b = target
        # so b = target - a
        # we use a hashmap and store the number as the key and the index as the value
        
        result = []
        numsMap = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in numsMap:
                return [i, numsMap[target - nums[i]]]
            else:
                numsMap[nums[i]] = i
         
        
        # we will neven reach here since every input will have a unique solution
        # simply return 
        
        return
        
        # time complexity O(n)
        # space complexity O(n)