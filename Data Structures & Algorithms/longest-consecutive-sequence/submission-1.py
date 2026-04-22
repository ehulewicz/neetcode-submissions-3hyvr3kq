class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        nums = set(nums)
        longest = 1

        for n in nums:
            if n - 1 not in nums:
                length = 1
                curr = n

                while curr + 1 in nums:
                    length += 1
                    curr = curr + 1

                longest = max(longest, length)

        return longest