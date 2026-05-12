class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices) - 1, 0, -1):
            best_profit = max(best_profit, prices[i] - min(prices[:i]))
        return best_profit