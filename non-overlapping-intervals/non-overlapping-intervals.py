# The decision to keep the interval with the smaller end time (by moving the left pointer to right) is a key strategy to minimize future overlaps.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if we have only 1 interval, it is a non overlapping interval
        if len(intervals) == 1: 
            return 0

        # sort the intervals based on the start
        intervals.sort(key = lambda i : i[0])
        result = 0    
        left, right = 0, 1

        while right < len(intervals):
            # start of current interval is less than end of interval corresponding to left
            if intervals[right][0] < intervals[left][1]:
                result += 1
                if intervals[left][1] > intervals[right][1]:
                    # keep the left pointer on an interval which has a lower end time
                    # this will ensure that out of the overlapping intervals, the 
                    # interval will the larger end time is eliminated
                    # larger end time will lead to more overlapping between remaining intervals
                    left = right

            else:
                left = right    

            right += 1

        return result    
        
