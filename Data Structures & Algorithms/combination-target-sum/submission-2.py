class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        # curr is a solution up to that point
        def dfs(start, curr, target):
            if target == 0:
                res.append(curr)
            if target > 0:
                for i in range(start, len(nums)):
                    temp = curr + [nums[i]]
                    dfs(i, temp, target - nums[i])
                    
        dfs(0, [], target)
        return res