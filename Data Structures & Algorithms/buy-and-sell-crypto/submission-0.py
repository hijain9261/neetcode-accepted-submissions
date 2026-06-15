class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_till_now = prices[0]
        max_profit = 0
        for price in prices:
            if min_till_now > price:  
                min_till_now = price
            
            profit = price - min_till_now
            if max_profit < profit:
                max_profit = profit

        return max_profit
            


        