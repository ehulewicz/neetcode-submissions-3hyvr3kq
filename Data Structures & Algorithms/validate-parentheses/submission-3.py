class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l == 0 or l % 2 == 1:
            return False

        close_to_open = {
            '}' : '{',
            ']' : '[',
            ')' : '(',
        }

        stack = []
        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if not stack or stack[-1] != close_to_open[c]:
                    return False
                stack.pop()
        return not stack