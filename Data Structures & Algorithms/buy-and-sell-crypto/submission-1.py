class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [10, 1, 5, 6, 7, 1]
        # On any day, the best buy price is the minimum day before that day
        # profit is the minimum price before that day, 
        max_profit = 0 
        min_price = float('inf')

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(price, min_price)
        
        return max_profit

        