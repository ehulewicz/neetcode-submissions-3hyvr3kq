class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        for i in range(32):
            if (1<<i) & n:
                counter += 1
        
        return counter