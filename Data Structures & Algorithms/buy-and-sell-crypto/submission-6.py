class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0

        i = 0

        max_value = 0
        for j in range(len(prices)):
            #max_value = max(max_value, prices[j]-prices[i])
            if prices[j] < prices[i]:
                i = j
            max_value = max(max_value, prices[j]-prices[i])
        
        print(i)
        print(j)
        return max_value
        