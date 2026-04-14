class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        
        def countLetters(string):
            chars = {}
            for c in string:
                if c in chars:
                    chars[c] += 1
                else:
                    chars[c] = 1
            return chars

        sChars = countLetters(s)
        tChars = countLetters(t)
        
        return sChars == tChars