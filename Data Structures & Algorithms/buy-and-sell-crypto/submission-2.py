class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            # Current price is the selling price
            sell = prices[i]

            # Find the best buying price before today
            min_price = min(min_price, sell)

            # Calculate today's possible profit
            profit = sell - min_price

            max_profit = max(max_profit, profit)

        return max_profit