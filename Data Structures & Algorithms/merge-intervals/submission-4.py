class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key=lambda i: i[0] )
        res = [ intervals[0] ]

        for i in range( 1, len( intervals ) ):
            val = intervals[i]

            if res[-1] == val:
                continue

            if val[0] > res[-1][1] or res[-1][0] > val[1]:
                res.append( val )
            else:
                res[-1] = [min( res[-1][0], val[0] ), max( res[-1][1], val[1] )]
        
        return res