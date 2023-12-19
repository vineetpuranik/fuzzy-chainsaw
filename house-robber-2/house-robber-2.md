## House Robber 2

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100

## Algorithm
Since the houses are arranged in a circle now which is the variation for this problem, we cannot rob both the first house and the last house.
Hence, we break our problem into 2 sub problems
Sub problem 1 We calculate the max amount of money the robber can get by robbing houses 1 .. n - 1 
Sub problem 2 We calculate the max amount of money the robber can get by robbing houses 2 .. n
The result will be the maximum amount from sub-problem 1 and sub-problem 2
