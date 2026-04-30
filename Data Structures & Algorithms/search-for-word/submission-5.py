class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(word_idx, i, j, seen):
            if word_idx == len(word):
                return True
            if (i < 0 or j < 0 or i >= m or j >= n or
                word[word_idx] != board[i][j] or word[word_idx] == '#'):
                return False

            board[i][j] = '#'

            if dfs(word_idx + 1, i - 1, j, seen):
                return True
            if dfs(word_idx + 1, i + 1, j, seen):
                return True
            if dfs(word_idx + 1, i, j - 1, seen):
                return True
            if dfs(word_idx + 1, i, j + 1, seen):
                return True

            board[i][j] = word[word_idx]
            return False

        for i in range(m):
            for j in range(n):
                seen = set()
                res = dfs(0, i, j, seen)
                if res == True:
                    return True
        return False