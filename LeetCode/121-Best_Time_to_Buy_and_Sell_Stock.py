class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimumPrice = 10001

        for p in prices:
            diff = p - minimumPrice
            if max_profit < diff:
                max_profit = diff

            if minimumPrice > p:
                minimumPrice = p

        return max_profit
