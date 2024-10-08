class Solution(object):
    def maxProfit(self, prices):
        minprice = float('inf')
        maxprofit = 0

        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit
        
