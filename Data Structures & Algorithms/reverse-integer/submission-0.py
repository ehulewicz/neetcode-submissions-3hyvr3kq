class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_pos = x > 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            res = (res * 10) + digit
            x //= 10

        if is_pos:
            if res > (2 ** 31) - 1:
                return 0
            return res
        
        res *= -1
        if res < -1 * (2 ** 31):
            return 0
        return res