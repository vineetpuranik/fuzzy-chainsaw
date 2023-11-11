###  Meeting Rooms

> Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

### Examples


> Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false


> Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


### Algorithm
1. Sort the intervals based on start time : O(nlogn)
2. Iterate through the sorted intervals and return false if the endtime of meeting 1 > start time of meeting 1 : O(n)

