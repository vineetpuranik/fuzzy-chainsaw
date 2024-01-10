class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Sub problem definition
        # Let L[i] correspond to the length of the LIS for the first i elements including the ith element

        # Recurrence relations
        # L[1] = 1
        # L[i] = 1 + max (L[i], L[i] + L[j]) if nums[j] < nums[i]
        # 0 <= i < n
        # j runs from 0 to i - 1
        # 0 <= j <= i - 1
        # Essentially the current element will always be included in the LIS. Additionally we cheock all the other elements before i which are less than it and choose the length of LIS from that element

        if len(nums) == 1:
            return 1

        # set all entries in L to 0 initially
        L = [0] * len(nums)

        L[0] = 1

        for i in range(1, len(nums)):
            # initially set the current entry to 1
            L[i] = 1

            # check all the i - 1 entries that are less than the ith element
            for j in range(0, i):
                if nums[i] > nums[j]:
                    L[i] = max(1 + L[j], L[i])

        # get the max LIS from all the entries
        result = 1
        for i in range(len(L)):
            result = max(result, L[i])

        return result 
