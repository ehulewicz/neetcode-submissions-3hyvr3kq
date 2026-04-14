class Solution:
    def countBits(self, n: int) -> List[int]:
        solution = []

        for i in range(n + 1):
            counter = 0
            for j in range(32):
                if (1<<j) & i:
                   counter += 1 
            solution.append(counter)
        
        return solution