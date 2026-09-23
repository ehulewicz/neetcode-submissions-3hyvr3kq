class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        memo = [[0] * (target + 1) for _ in range(len(nums) + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if memo[i][target] != 0:
                return memo[i][target]

            memo[i][target] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            
            return memo[i][target]

        return dfs(0, target)