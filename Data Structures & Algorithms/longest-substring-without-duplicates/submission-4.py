class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len( s ) <= 1:
            return len( s )
        
        seen = {}
        longest = 0

        i = 0

        for j in range( len( s ) ):
            if s[j] in seen:
                i = max( seen[s[j]] + 1, i )

            seen[s[j]] = j
            longest = max( longest, j - i + 1 )
            j += 1

        return longest