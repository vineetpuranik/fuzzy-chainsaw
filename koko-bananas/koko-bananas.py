# https://leetcode.com/problems/koko-eating-bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # piles represent an array where each item in the array is the number of bananas in that pile
        # the guards have gone and they will come back in h hours. h is the second input to our program along with piles
        # bananas per hour eating speed is k which is what we have to determine. 
        # if a pile has number of bananas less than k then koko will finish the pile and will not eat any more bananas in that hour.
        # we have to determine the min value of k such that koko can finish all the piles before the guards come back. 
        # number of piles <= h (time in hours that guards are gone)
        
        
        # piles = [3, 6, 7, 11] , h = 8
        # k can be between 1 and 11. if k is 11 koko can finish all the piles in 4 hours but we want the min value of k
        
        
        # Brute force : Start from 1 and continue until we find a k. k is bounded between 1 and max(piles)
        # O(max(piles) * n)
        # Time limit exceed error with brute-force approach
        
        """
        # initialize upperBound for our iteration
        upperBound = max(piles)
        # initialize a result variable
        result = 0
        
        for i in range(1, upperBound + 1):
            
            # iterate through every banana pile and get the number of hours with current i to finish every pile
            # add this number and check with h
            # return the first value of i where the sum of pile eating time for given i is less than equal to k
            total_time = 0
            for pile in piles:
                current_time = math.ceil(pile / i)
                total_time += current_time
            
            if total_time <= h :
                result = i
                break
                
        return result
        
        """
        
        # Binary Search approach
        # O(log(piles) * n) Time complexity
        # here instead of checking very possible k from 1..max(piles) we employ binary search technique
        # start with left = 1 and right to be max(piles)
        # calculate mid based on binary search method. 
        # get the value of k when eating speed is mid.
        # if this results in total number of hours > h then it means we will have dial up the eating speed so we shift l to mid and maintain the current result which is min of current result and any prev result
        # if this results in total number of hours <= h then it means we will can dial down the eating speed so shift r to mid.
        # if l and r pointers meet or they cross each other then return the current result. 
        
        # l pointer at 1 and r pointer at max(piles)
        l, r = 1, max(piles)
        
        # initially result is initialized to max(piles)        
        result = max(piles)
        
        # binary search for results
        while l <= r : 
            mid = (l + r) // 2 # (take the floor of the division)
            current_time = 0
            for pile in piles:
                pile_time = math.ceil(pile/mid)
                current_time += pile_time
            
            if current_time > h : 
                # in this case we need to dial up the eating speed
                l = mid + 1
            else:
                r = mid - 1
                result = min(result, mid)
        
        return result
                
