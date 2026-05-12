class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        current_max = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                current_max = max(current_max, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return current_max