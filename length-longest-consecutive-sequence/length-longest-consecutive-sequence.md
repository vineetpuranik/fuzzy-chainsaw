## Length of the longest consecutive sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

## Constraints 
0 <= nums.length <= 105
-109 <= nums[i] <= 109

## Algorithm 
We can sort the input elements and check for the length of the longest consecutive sequence in O(nlogn) time
Goal is to provide a linear time O(n) solution for this problem. 

1. Consider nums = [100,4,200,1,3,2]
2. This input comprises of 3 consecutive sequences : [100] , [200], [1, 2, 3, 4]
3. The output here should be 4 for the sequence [1, 2, 3, 4]
4. This gives us an intuition that every element in nums could be either the start of the consecutive sequence or it could be part of the consecutive sequence.
5. So we add all the elements of nums in a set
6. Then for every element in nums if current element - 1 nums is not in nums then it means that the current element is the start of a new sequence.
7. In this case we go on incrementing current element + 1 .. + 2 so on until we no longer are able to form a sequence.
8. Using this technique we ensure that we look at each element in nums atmost twice and hence we come down to a O(n) solution
   
