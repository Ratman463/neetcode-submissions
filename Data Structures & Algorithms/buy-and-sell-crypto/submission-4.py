class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        [i, j] = [0, 0]
        head = prices[i]
        tail = prices[j]
        
        while j < len(prices):
            while tail >= head and j < len(prices) - 1:
                tail = prices[j]
                max_profit = max(max_profit, tail - head)
                j += 1
                
            while tail < head and i < j:
                print(f"i: {i}")
                head = prices[i]
                max_profit = max(max_profit, tail - head)
                i += 1

            tail = prices[j]
            max_profit = max(max_profit, tail - head)
            j += 1
            
        return max_profit