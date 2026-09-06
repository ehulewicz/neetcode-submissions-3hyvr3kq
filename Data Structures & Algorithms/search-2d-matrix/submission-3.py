class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0

        while row < len(matrix):
            print(row)
            if matrix[row][0] == target:
                return True
            if matrix[row][0] > target:
                row -= 1
                break
            row += 1

        row = min(row, len(matrix) - 1)
        for num in matrix[row]:
            if num == target:
                return True
        return False