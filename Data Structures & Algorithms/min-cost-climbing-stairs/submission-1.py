class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(n) = min(c(n-1)+f(n-1), c(n-2)+f(n-2))
        n = len(cost)
        minCosts = [0] * (n+1)

        for i in range(2, n+1):
            minCosts[i] = min(minCosts[i-1] + cost[i-1], minCosts[i-2] + cost[i-2])

        # top is n + 1       
        return minCosts[-1]
        
