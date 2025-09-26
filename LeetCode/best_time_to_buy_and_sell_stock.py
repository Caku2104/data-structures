# LeetCode '121. Best Time to Buy and Sell Stock' Problem

class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        max_profit = 0

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                profit = price - minimum
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit