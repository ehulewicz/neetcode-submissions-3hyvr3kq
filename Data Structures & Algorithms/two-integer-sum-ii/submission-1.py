class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i, n in enumerate(numbers):
            find = target - n
            if find in mp:
                return [mp[find] + 1, i + 1]
            mp[n] = i
        return []