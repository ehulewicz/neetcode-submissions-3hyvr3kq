import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        dp = [[0]*(n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 2:
                    dp[i][j] = 1
                elif i == m - 2 and j == n - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j]

        return dp[0][0]