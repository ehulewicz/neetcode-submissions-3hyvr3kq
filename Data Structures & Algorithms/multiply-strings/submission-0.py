class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def to_int(num: str) -> int:
            res = 0

            for n in num:
                n = ord(n) - ord("0")

                res *= 10
                res += n
            return res

        num = to_int(num1) * to_int(num2)

        return str(num)