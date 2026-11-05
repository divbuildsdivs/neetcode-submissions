class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newIntervals = []
        intervals.sort()
        interval = intervals.pop(0)
        
        while len(intervals) > 0:
            if interval[1] < intervals[0][0]:
                newIntervals.append(interval)
                interval = intervals.pop(0)
            else:
                interval[0] = min(interval[0], intervals[0][0])
                interval[1] = max(interval[1], intervals[0][1])
                intervals.pop(0)
            
        newIntervals.append(interval)

        return newIntervals