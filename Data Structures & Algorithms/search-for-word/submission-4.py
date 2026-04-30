class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def recurse(word_idx, i, j, seen):
            if (i, j) in seen:
                return False
            print(word[word_idx], board[i][j], i, j, word_idx, len(word) - 1)

            if word_idx == len(word) - 1 and word[word_idx] == board[i][j]:
                print('return')
                return True
            if word[word_idx] != board[i][j]:
                return False

            seen.add((i, j))

            if i > 0:
                if recurse(word_idx + 1, i - 1, j, seen):
                    return True
            if i < m - 1:
                if recurse(word_idx + 1, i + 1, j, seen):
                    return True
            if j > 0:
                if recurse(word_idx + 1, i, j - 1, seen):
                    return True
            if j < n - 1:
                if recurse(word_idx + 1, i, j + 1, seen):
                    return True

            seen.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                seen = set()
                res = recurse(0, i, j, seen)
                if res == True:
                    return True
        return False