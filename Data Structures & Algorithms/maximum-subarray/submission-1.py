class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len( nums ) == 1:
            return nums[0]
        
        top = max( nums )
        if top <= 0:
            return top

        submax = nums[0]
        window = nums[0] if nums[0] > 0 else 0

        for i in range( 1, len( nums ) ):
            n = nums[i]
            if n < 0:
                submax = max( submax, window )
            
            window += n
            if window < 0:
                window = 0
            
        return max( submax, window )