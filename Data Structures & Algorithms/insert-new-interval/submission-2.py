class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        res = []
        while len(intervals) > 0:
            
            if intervals[0][1] < newInterval[0]:
                res.append(intervals.pop(0))
            elif newInterval[1] < intervals[0][0] :
                res.append(newInterval)
                res.extend(intervals)
                return res
            else:
                newInterval[0] = min(newInterval[0], intervals[0][0])
                newInterval[1] = max(newInterval[1], intervals[0][1])
                intervals.pop(0)
        res.append(newInterval)

        return res
        