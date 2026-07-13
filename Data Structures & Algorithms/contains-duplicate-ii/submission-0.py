class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = defaultdict(int)

        l = 0
        for r in range(len(nums)):
            if window[nums[r]] > 0:
                return True

            window[nums[r]] += 1
            
            if abs(r - l) == k:
                window[nums[l]] -= 1
                l += 1
        
        return False