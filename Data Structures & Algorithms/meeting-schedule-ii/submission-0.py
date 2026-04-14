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
        
        intervals.sort( key=lambda x: x.start )
        minHeap = []

        for i in intervals:
            if minHeap and i.start >= minHeap[0]:
                heapq.heappop( minHeap )
            heapq.heappush( minHeap, i.end )
        
        return len( minHeap )