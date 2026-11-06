class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        N = len(intervals)
        if N <= 1:
            return 0
        interval = intervals.pop(0)
        newIntervals = []

        while len(intervals) > 0:
            if interval[1] > intervals[0][0]:
                if intervals[0][1] > interval[1]:
                    intervals.pop(0)
                else:
                    interval = intervals.pop(0)
                
            else:
                newIntervals.append(interval)
                interval = intervals.pop(0)
           
        newIntervals.append(interval)
        return N - len(newIntervals)