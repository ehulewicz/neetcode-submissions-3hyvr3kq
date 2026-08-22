class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        
        def dfs(r, c):
            if (r, c) in seen:
                return
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
                return

            seen.add((r, c))

            if grid[r][c] == "1":
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in seen:
                    continue
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res