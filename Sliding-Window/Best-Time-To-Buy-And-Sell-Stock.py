class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # Keep track of the highest current profit, and the current lowest price for comparison
        highestProfit = 0
        lowestPrice = prices[0]

        for price in prices:

            # If we find a new low price, update lowest price and continue to find the profits from that point
            if price < lowestPrice:
                lowestPrice = price
            
            # Calculate the profit at that time vs the lowest price, and update our highest profit if larger
            else:
                profit = price - lowestPrice
                if profit > highestProfit:
                    highestProfit = profit
        
        return highestProfit