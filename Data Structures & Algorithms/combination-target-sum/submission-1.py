class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        
        # curr is a solution up to that point
        def dfs(curr, target):
            if target == 0:
                ans = tuple(sorted(curr))
                if ans not in seen:
                    seen.add(ans)
            if target > 0:
                for n in nums:
                    temp = curr + [n]
                    dfs(temp, target - n)
        dfs([], target)

        res = []
        for s in seen:
            res.append(list(s))
        return res