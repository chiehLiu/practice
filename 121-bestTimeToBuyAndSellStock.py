class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # One pass solution
        # Keep track of the minimum price and the maximum profit
        # Iterate through the list of prices
        # Update the minimum price and the maximum profit

        # if you don't remember the solution, you can draw a x, y axis, x is the days, y is the price
        # keep track of the minimum price
        # and since the days iterate through the price list, the maximum profit is the maximum difference between the current price and the minimum price

        # Time complexity: O(n)
        # Space complexity: O(1)
        
        # Initialize the maximum profit to negative infinity and the minimum price to positive infinity
        # so that these two variables can be updated in the loop
        max_profit = float('-inf')
        min_price = float('inf')

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit