## House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
## Constraints
1 <= nums.length <= 100
0 <= nums[i] <= 400

## Examples
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

## Idea
1. Express the sub-problem in words : Let p(i) denote the max amount of money that can be robbed from the first i houses. 
2. Base cases : p(0) = nums(0) ; i = 0 , p(1) = max(p(0), p(1)) ; i = 1
3. Recursive relatino : p(i) = max(p(i-1), (nums(i) + p(i - 2))) ; 2 <= i < nums.length