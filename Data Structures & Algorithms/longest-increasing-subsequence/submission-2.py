class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len( nums ) == 1:
            return 1

        mem = [1] * len( nums )
        
        for i in range( len( nums ) - 1, -1, -1 ):
            for j in range( i + 1, len( nums ) ):  
                if nums[i] < nums[j]:
                    mem[i] = max( mem[i], 1 + mem[j] )

        return max( mem )