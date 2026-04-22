class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins = sorted(coins, reverse=True)
        res = float('inf')

        def dfs(start, curr, target):
            nonlocal res
            
            if target == 0:
                res = min(res, curr)
                return
            if curr >= res:
                return

            if target > 0:
                for i in range(start, len(coins)):
                    dfs(i, curr + 1, target - coins[i])
        
        dfs(0, 0, amount)
        if res == float('inf'):
            return -1
        return res