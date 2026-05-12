class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0

        for i, buy_price in enumerate(prices):
            if i == len(prices) - 1:
                break
            
            current_max = max(current_max, max(prices[i + 1:]) - buy_price)
        
        return current_max