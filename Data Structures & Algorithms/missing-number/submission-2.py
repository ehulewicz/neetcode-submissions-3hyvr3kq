class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)

        for i in range(len(nums) + 1):
            if i not in seen:
                return i