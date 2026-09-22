class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]):
            x, y = point

            return math.sqrt(x ** 2 + y ** 2)

        heap = []

        for p in points:
            heapq.heappush( heap, ( distance( p ), p ) )

        res = []
        for i in range(k):
            res.append( heapq.heappop( heap )[1] )

        return res