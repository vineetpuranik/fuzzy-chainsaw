class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # unsorted array of integer nums
        # return the length of the longest consecutive elements sequence

        # if we sort the elements then it will be pretty straightforward in O(nlogn) time
        # with sorting
        # if len(nums) == 0: 
            # return 0

        # intialize result to 1
        # result = 1
        # tempResult = 1
        # sort nums
        # nums.sort()

        # start with the 2nd element in nums
        # for i in range(1, len(nums)):
            # current element is the next in sequence
            # if nums[i] == nums[i - 1] + 1:
                # tempResult += 1
                # print(tempResult)
            # current element is the start of the next sequence    
            # else:
                # result = max(result, tempResult)
                # tempResult = 1

        # return max(result, tempResult)

        # In O(n) time
        # if len(nums) == 0 then  we will return 0
        if len(nums) == 0:
            return 0

        # add the input numbers to a set
        # adding nums to a set will take O(n) time
        # looking up if an element exists in the set will take O(1) time
        numsSet = set(nums)
        result = 1
        
        for i in range(len(nums)):
            # check if the current element is the start of a new sequence
            # this will be true if current element - 1 is not in the numsSet
            # if current element - 1 is in numsSet then current element is not a start of a new sequence
            # this will ensure that we are iterating the elements in a sequence only once for the inner while loop    
            if nums[i] - 1 not in numsSet:
                tempResult = 1
                currentElement = nums[i]
                nextElement = currentElement + 1
                while nextElement in numsSet:
                    tempResult += 1
                    nextElement += 1
                result = max(result, tempResult)

        return result


        
