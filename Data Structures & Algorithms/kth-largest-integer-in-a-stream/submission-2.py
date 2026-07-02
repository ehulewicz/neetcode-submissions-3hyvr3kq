class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top_k = []
        self.k = k

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if not self.top_k:
            self.top_k.append(val)
            return self.top_k[-1]

        i = 0
        inserted = False
        while not inserted and i < len(self.top_k):
            if val > self.top_k[i]:
                self.top_k.insert(i, val)
                inserted = True
            i += 1

        if not inserted and len(self.top_k) < self.k:
            self.top_k.append(val)
        if len(self.top_k) > self.k:
            self.top_k.pop()

        return self.top_k[-1]
            
        