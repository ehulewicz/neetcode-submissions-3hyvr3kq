class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                cell = board[row][i]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        for col in range(9):
            seen = set()
            for i in range(9):
                cell = board[i][col]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        for square in range(9):
            seen = set()
            row = (square // 3) * 3
            col = (square % 3) * 3
            for m in range(3):
                for n in range(3):
                    cell = board[row + m][col + n]
                    if cell == ".":
                        continue
                    if cell in seen:
                        return False
                    seen.add(cell)
                
        return True