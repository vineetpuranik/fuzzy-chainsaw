## Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## Examples 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

## Constraints
n == height.length
2 <= n <= 105
0 <= height[i] <= 104

## Algorithm 
Brute force : O(n^2) -> Check area for every pair of heights and return the max area
Ideal solution : Set 2 pointers left to 0 and right to len - 1. Calculate the area and update the pointer which has less height from amongst left and right pointers. O(n)
