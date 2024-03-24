class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # prefix multiplication
        for i in range(len(nums)):
            if (i == 0):
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]
              
        # postfix multiplication
        for i in range(len(nums)-1, -1, -1):
            if (i == len(nums) - 1):
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i] 
        # output
        # first element = postfix of second element
        # last element = prefix of second last element
        # other elements = prefix of prev element * post fix of next element
        for i in range(len(nums)):
            if (i == 0):
                output[i] = postfix [i + 1]
            elif (i == len(nums) - 1):
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * postfix [i + 1]

        return output
