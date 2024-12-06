class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                if max_profit < profit:
                    max_profit = profit

        return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)