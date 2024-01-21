class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums array of integer
        # nums will have atleast 3 numbers
        # return triplets that sum up to 0 

        # -4, -1, -1, 0, 1, 2 
        # sort the input array
        # iterate element by element. From 2nd element onwards check if the current
        # element is not equal to the previous element. If it is then skip it    
        # because we want to avoid duplicate answers in the solution set. 
        # set left to i + 1 and right to len - 1
        # iterate till left < right
        # set target = 0 - nums[i]
        # the problem now reduces to Two Sum II
        # we also have to shift the left pointer or the right pointer when we get a result
        # after shifting one important step to consider is that we have to again compare the left and left - 1 so that they are not duplicates
        # if they are then we keep shifting until left < right

        # Time complexity O(n^2)

        result = []

        # sort the input elements
        nums.sort()

        for i in range(len(nums)):
            current = nums[i]
            target = 0 - nums[i]

            # check if current = previous 
            # if yes then skip this iteration
            if i > 0 : 
                if current == nums[i - 1]:
                    continue

            # set left and right pointers
            left , right  = i + 1, len(nums) - 1

            while left < right :

                # found 3 elements that add up to 0
                if nums[left] + nums[right] == target:
                    result.append([current, nums[left], nums[right]])
                    # here we can either shift the left pointer to the right
                    # or we can shift the right pointer to the left
                    left += 1

                    # when we shift the left pointer, we now have to 
                    # again check if the current value at left and left - 1
                    # is equal. we continue shifting until they are not the
                    # same. This is again to avoid duplicates.
                    
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                
                # current sum > target then shift right pointer by - 1
                elif nums[left] + nums[right] > target:
                    right -= 1   

                # current sum < target then shift left pointer by + 1       
                else:
                    left += 1

        return result    


