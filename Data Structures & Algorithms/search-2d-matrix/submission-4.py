class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1
        while l <= r:
            row = (l + r) // 2
            if target > matrix[row][-1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row - 1
            else:
                break

        if l > r:
            return False
        
        l, r = 0, COLS - 1
        while l <= r:
            col = (l + r) // 2
            if target > matrix[row][col]:
                l = col + 1
            elif target < matrix[row][col]:
                r = col - 1
            else:
                return True
        return False