class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice  = prices[0]
        maxprofit = 0

        for i in prices:
            if i < minprice:
                minprice = i
            profit = i - minprice
            maxprofit = max(maxprofit , profit)
       
        return maxprofit
        