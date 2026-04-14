import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = Counter(nums)
        heap = []

        for num, count in counter_map.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        print( counter_map )
        return [num for count, num in heap]