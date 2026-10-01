class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 101
        profit = 0

        for i in prices:
            if i < low:
                low = i
            else:
                profit = max(profit, i-low)

        return profit