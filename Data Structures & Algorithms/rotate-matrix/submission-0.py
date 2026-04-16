class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 1:
            return
        matrix.reverse()

        for m in range(len(matrix) - 1):
            for n in range(m + 1, len(matrix)):
                matrix[m][n], matrix[n][m] = matrix[n][m], matrix[m][n]