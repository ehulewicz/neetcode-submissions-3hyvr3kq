"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
    
        min_start = float('inf')
        max_end = 0

        starts = set()
        ends = set()

        for i in intervals:
            start = i.start
            end = i.end

            if start in starts or end in ends:
                return False

            starts.add(start)
            ends.add(end)

            min_start = min(min_start, start)
            max_end = max(max_end, end)

        allow_schedule = True
        for i in range(min_start, max_end + 1):
            if i in starts and i in ends:
                allow_schedule = False
            elif i in starts:
                if not allow_schedule:
                    return False
                allow_schedule = False
            elif i in ends:
                allow_schedule = True

        return True


