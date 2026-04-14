class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len( s ) <= 1:
            return len( s )
        
        seen = {}
        longest = 0

        i, j = 0, 0
        curr = 0

        while i + j < len( s ):
            if s[i + j] not in seen:
                seen[s[i + j]] = i + j
                j += 1
            else:
                longest = max( longest, len( seen ) )
                i = seen[s[i + j]] + 1
                j = 0
                seen = {}

        return max( longest, len( seen ) )