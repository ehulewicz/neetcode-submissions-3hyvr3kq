class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if (1<<i) & n:
                result += 2 ** (31 - i)
        return result