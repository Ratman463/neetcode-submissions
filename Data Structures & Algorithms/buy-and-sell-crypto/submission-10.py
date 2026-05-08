class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0 # buy date
        while i < len(prices):
            j = i
            while j < len(prices) and prices[j] >= prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
            i = j
        return max_profit