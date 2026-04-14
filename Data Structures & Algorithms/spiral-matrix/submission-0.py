class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len( matrix )
        cols = len( matrix[0] )

        if rows == 1 and cols == 1:
            return [matrix[0][0]]

        horizontal = True
        step = 1
        
        seen = set()
        res = []

        m, n = 0, -1
        for _ in range( rows * cols ):
            if horizontal:
                n += step
            else:
                m += step

            res.append( matrix[m][n] )
            seen.add( (m, n) )
            print( (m, n) )

            if horizontal:
                if n + step < 0 or n + step == len( matrix[0] ) or (m, n + step) in seen:
                    horizontal = False
            else:
                if m + step < 0 or m + step == len( matrix ) or (m + step, n) in seen:
                    horizontal = True
                    step *= -1

        return res
            