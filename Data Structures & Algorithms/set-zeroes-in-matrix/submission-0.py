class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_columns = set()
        
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if matrix[m][n] == 0:
                    zero_rows.add(m)
                    zero_columns.add(n)

        for m in zero_rows:
            matrix[m] = [0] * len(matrix[m])

        for n in zero_columns:
            for m in range(len(matrix)):
                matrix[m][n] = 0