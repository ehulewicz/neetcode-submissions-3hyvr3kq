class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_idx = 0
        best_len = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if best_len < (r - l + 1):
                    best_len = (r - l + 1)
                    best_idx = l
                l -= 1
                r += 1
                
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if best_len < (r - l + 1):
                    best_len = (r - l + 1)
                    best_idx = l
                l -= 1
                r += 1

        return s[best_idx:(best_idx + best_len)]