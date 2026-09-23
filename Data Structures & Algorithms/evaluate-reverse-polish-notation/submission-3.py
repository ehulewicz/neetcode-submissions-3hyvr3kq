from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        def operate(l, r, sym):
            l = int(l)
            r = int(r)

            if sym == '+':
                return l + r
            if sym == '-':
                return l - r
            if sym == '*':
                return l * r
            if sym == '/':
                return l / r

        stack = []

        for t in tokens:
            try:
                num = int(t)
                stack.append(num)
            except ValueError:
                r = stack.pop()
                l = stack.pop()
                stack.append(operate(l, r, t))

        return int(stack.pop())