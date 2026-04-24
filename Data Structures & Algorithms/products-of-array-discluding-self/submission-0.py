class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        res = [0] * len(nums)

        for n in nums:
            if n == 0:
                zeros += 1

        if zeros > 1:
            return res

        zero_idx = -1
        for i, n in enumerate(nums):
            if n != 0:
                product *= n
            else:
                zero_idx = i

        if zeros == 1:
            res[zero_idx] = product
            return res

        for i, n in enumerate(nums):
            res[i] = product // n
        return res