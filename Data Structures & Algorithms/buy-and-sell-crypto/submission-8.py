class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0 # buy date
        t = 0
        while i < len(prices) and t < 10:
            j = i
            # print(f"i:{i}")
            # print(f"j:{j}")
            t+=1
            while j < len(prices) and prices[j] >= prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
            i += 1
        return max_profit