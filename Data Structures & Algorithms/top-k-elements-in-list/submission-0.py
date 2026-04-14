import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}

        for num in nums:
            if num not in counter_map:
                counter_map[num] = 0
            else:
                counter_map[num] += 1

        heap = []
        for num, count in counter_map.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]