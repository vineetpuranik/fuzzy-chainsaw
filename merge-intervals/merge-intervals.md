## Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Algorithm
1. First sort all the intervals based on the start times.
2. intervals.sort(key = lambda i : i[0])
3. Add the first interval to the results list
4. Iterate all the sorted intervals from the second interval to the last interval
5. If startOfCurrent <= endOfLast (results[-1][1]) then the current interval and the latest interval in the results overlap. Hence, we have to merge them
6. Merging = results[-1][1] = max(currentEnd, results[-1][1]). No need to update the start because of sorting
7. If intervals do not overlap directly add the current interval to the end of our output list.
8. Time complexity : 0(nlogn) because sorting dominates
   
