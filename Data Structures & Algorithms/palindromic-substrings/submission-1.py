class Solution:
    def countSubstrings(self, s: str) -> int:
        # Last digit not hit in loop
        counter = 1
        def recurse(l, r):
            if l < 0 or r > len(s) - 1:
                return
            nonlocal counter

            if s[l] == s[r]:
                counter += 1
                recurse(l - 1, r + 1)

        for i in range(len(s) - 1):
            recurse(i, i)
            recurse(i, i + 1)

        return counter