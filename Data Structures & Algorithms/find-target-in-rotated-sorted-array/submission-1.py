class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m

        pivot = i

        def binary_search(i, j):
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if j <= i or j - i == 1:
                return -1
            
            m = (i + j) // 2
            if nums[m] > target:
                return binary_search(i, m - 1)
            return binary_search(m, j)

        res = binary_search(0, pivot)
        if res != -1:
            return res

        return binary_search(pivot, len(nums) - 1)