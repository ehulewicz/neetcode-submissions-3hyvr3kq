class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len( heights ) - 1

        max_water = right * min( heights[left], heights[right] )
        print( max_water )

        while left != right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
            max_water = max( max_water, ( right - left ) * min( heights[left], heights[right] ) )
            print( max_water )
            print( heights[left] )
            print( heights[right] )
            print()
        
        return max_water
        
        