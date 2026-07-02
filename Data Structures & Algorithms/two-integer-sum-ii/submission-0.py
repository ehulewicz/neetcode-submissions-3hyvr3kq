class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        find = {}

        for i, n in enumerate(numbers):
            find[target - n] = i

        for i, n in enumerate(numbers):
            if n in find:
                idx = find[n]
                if i != idx:
                    return [i + 1, idx + 1]