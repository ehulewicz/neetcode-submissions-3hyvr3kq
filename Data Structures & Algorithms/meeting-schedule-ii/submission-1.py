import numpy as np

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len( intervals ) == 0:
            return 0
        
        starts = sorted( [i.start for i in intervals] )
        ends = sorted( [i.end for i in intervals] )

        res, count = 0, 0
        i, j = 0, 0

        while i < len( intervals ):
            if starts[i] < ends[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max( res, count )

        return res
        

