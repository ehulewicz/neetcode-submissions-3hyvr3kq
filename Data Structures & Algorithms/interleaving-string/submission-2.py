class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        mem = {}
        def dfs(a, b, c) -> bool:
            if c == len(s3):
                return a == len(s1) and b == len(s2)
            if (a, b, c) in mem:
                return mem[(a, b, c)]

            res = False

            if a < len(s1) and s1[a] == s3[c]:
                res |= dfs(a + 1, b, c + 1)

            if b < len(s2) and s2[b] == s3[c]:
                res |= dfs(a, b + 1, c + 1)
            
            mem[(a, b, c)] = res
            return res

        return dfs(0, 0, 0)