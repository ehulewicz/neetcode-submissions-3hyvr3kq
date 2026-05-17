class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        longest = 0
        for w in wordDict:
            longest = max(longest, len(w))
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True

            # watch out for out of bounds
            substr = ''
            for j in range(i, min(len(s), i + longest + 1)):
                substr += s[j]
                if substr in wordSet:
                    if dfs(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)