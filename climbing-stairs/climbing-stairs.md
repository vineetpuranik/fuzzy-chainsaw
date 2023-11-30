## Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Examples
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

## Algorithm
1. Let r[i] represent the distinct ways for climbing the first i stairs
2. r[0] = 0, r[1] = 1. r[2] = 2 -> Base Cases
3. r[i] = r[i - 2] + r[i - 1] ; 3 <= i <= n
4. We can reach the ith stair either from the i-2nd or the i-1st stair and hence the distinct ways to reach the ith stair = distinct ways to reach the i-2nd stair + distinct ways to reach the i -1st stair.