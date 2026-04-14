class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        best = 0
        low = float('inf')

        for i in range( 1, len( prices ) ):
            low = min(low, prices[i - 1])
            best = max(best, prices[i] - low) 

        return best