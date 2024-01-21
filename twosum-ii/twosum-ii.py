class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we will always have atleast 2 elements in our numbers list
        left, right = 0, len(numbers) - 1

        while left < right :
            currentSum = numbers[left] + numbers[right]
          
            # if currentSum > target then shift the right pointer by - 1
            if currentSum > target:
                right -= 1
              
            # if currentSum < target then shift the left pointer by +1  
            elif currentSum < target:
                left += 1
              
            # if we find target then return the result
            else:
                return [left + 1, right + 1]
