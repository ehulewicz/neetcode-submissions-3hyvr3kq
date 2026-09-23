class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if target != int(target):
            return False
        target = int(target)

        def recurse(vals, curr):
            if curr == target:
                return True
            if curr > target:
                return False

            for i in range(len(vals)):
                new_vals = vals.copy()
                val = curr + new_vals.pop(i)
                
                if recurse(new_vals, val):
                    return True
            return False

        return recurse(nums, 0)
