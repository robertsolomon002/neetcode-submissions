class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices) 

        if length < 2: 
            return 0

        res = 0

        left = 0
        right = 1

        while right < length:
            #We buy at left and sell at right
            profit = prices[right] - prices[left]
            res = max(res, profit)


            if prices[right] > prices[left]:
                right +=1
            else:
                left = right
                right = left +1

        return res



        