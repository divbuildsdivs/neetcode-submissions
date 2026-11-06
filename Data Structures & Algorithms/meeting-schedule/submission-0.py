"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
       
        intervals.sort(key=lambda x: x.start)
        if len(intervals) <= 1:
            return True

        interval = intervals.pop(0)
        while len(intervals) > 0:
            if interval.end > intervals[0].start:
                return False
            interval = intervals.pop(0)
        return True

