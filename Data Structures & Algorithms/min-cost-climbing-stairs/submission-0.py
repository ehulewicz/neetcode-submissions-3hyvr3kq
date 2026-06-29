class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        mem[len(cost)] = 0
        mem[len(cost) - 1] = cost[-1]

        for i in range(len(cost) - 2, -1, -1):
            mem[i] = cost[i] + min(mem[i + 1], mem[i + 2])

        return min(mem[0], mem[1])