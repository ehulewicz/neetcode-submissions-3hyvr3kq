class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        nums = sorted(nums)
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
            if nums[i] == nums[i - 1]:
                dp[i] = dp[i - 1]

        return max(dp)
        