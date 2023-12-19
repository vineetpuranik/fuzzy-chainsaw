class Solution:
    def rob(self, nums: List[int]) -> int:
        # since now the houses are arranged in circle, we cannot
        # rob both the first house
        # so we split our problems into two sub-problems
        # first rob houses 1 to n -1 and get the max money
        # then rob houses 2 to n and get the max money
        # return the maximum amount from both the scenarios as the answer
        
        def robLinear(n):
            if len(n) == 1:
                return n[0]

            r = [0 for _ in range(len(n))]
            r[0] = n[0]
            r[1] = max(n[0], n[1])
            
            for i in range(2, len(n)):
                r[i] = max (r[i - 1], (n[i] + r [i - 2] ))
                
            return r[-1]
        
        # if there is only 1 house to rob, 
        if len(nums) == 1:
            return nums[0]
        
        # return the maximum amount from robbing either 
        # houses 1 to n -1 or 2 to n
        
        return max(robLinear(nums[0:len(nums) - 1]) , robLinear(nums[1:len(nums)]))
