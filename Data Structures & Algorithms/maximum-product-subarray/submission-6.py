import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len( nums ) == 1:
            return nums[0]
        

        groups = []
        last_zero = None
        for i, n in enumerate( nums ):
            if n == 0:
                if last_zero:
                    groups.append( nums[last_zero + 1:i] )
                elif i != 0:
                    groups.append( nums[0:i] )
                last_zero = i
            elif i == len( nums ) - 1:
                last_zero = -1 if last_zero is None else last_zero
                groups.append( nums[last_zero + 1:] )
        
        # return count, first occurance, last occurance
        def count_negatives( group: List[int] ) -> tuple[int, int, int]:
            counter = 0
            first = None
            last = None
            for i, n in enumerate( group ):
                if n < 0:
                    counter += 1
                    if first is None:
                        first = i
                    last = i
                        
            return ( counter, first, last )

        max_prod = 0 if last_zero is not None else float('-inf')
        for g in groups:
            print(g)
            if len(g) == 1:
                max_prod = max( max_prod, g[0] )
                continue

            # of negatives
            count, first, last = count_negatives(g)

            if count % 2 == 0:
                max_prod = max( max_prod, math.prod( g ) )
            else:
                left = math.prod( g[:last] )
                right = math.prod( g[first + 1:] )
                max_prod = max( max_prod, left, right )
        return max_prod