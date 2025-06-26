"""
Submission Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1677645584
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            profit = prices[i] - buy_price
            max_profit = max(max_profit, profit)
        return max_profit
