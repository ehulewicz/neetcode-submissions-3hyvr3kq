import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            one = heapq.heappop_max(stones)
            two = heapq.heappop_max(stones)

            diff = abs(two - one)
            if diff > 0:
                heapq.heappush_max(stones, diff)
        
        return stones[0] if stones else 0