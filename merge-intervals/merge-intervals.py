class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # goal is to merge overlapping intervals
        # consider [1, 7], [3, 8]
        # this is an overlapping interval with a result [1, 8]
        # how to check : start of second <= end of first then they are overlappping
        

        if len(intervals) == 1:
            # there is only 1 interval
            return intervals

        mergedIntervals = []


        # first we will sort all the intervals based on the start of each interval
        intervals.sort(key = lambda i : i[0])

        # add the first element to the output
        mergedIntervals.append(intervals[0])

        # iterate from 2nd interval to the last
        for i in range(1, len(intervals)):
            currentStart = intervals[i][0]
            currentEnd = intervals[i][1]
            lastEnd = mergedIntervals[-1][1]
            # if intervals overlap
            if currentStart <= lastEnd:
                # we only need to update the end of the interval
                # this is because we had sorted the input
                mergedIntervals[-1][1] = max(lastEnd, currentEnd)

            # if intervals do not overlap
            else :
                mergedIntervals.append(intervals[i])    
        

        return mergedIntervals

        # time complexity : O(nlogn) dominated by the sorting step
        # space : O(n) since we have to return the results
