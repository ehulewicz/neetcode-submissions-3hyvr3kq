class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, prev, visited):
            if (r, c) in visited:
                return
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            if prev > heights[r][c]:
                return

            visited.add((r, c))
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)

        for r in range(m):
            dfs(r, 0, -1, pac)
            dfs(r, n - 1, -1, atl)
        for c in range(n):
            dfs(0, c, -1, pac)
            dfs(m - 1, c, -1, atl)

        res = []
        for p in pac:
            if p in atl:
                res.append([p[0], p[1]])
        return res