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
            print(c)
            if len(stack) == 0 or c not in close_to_open:
                print("push")
                stack.append(c)
            else:
                if stack[-1] == close_to_open[c]:
                    print("pop");
                    stack.pop()
                else:
                    return False
        return not stack