class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        p_len = len(prices)
        dp = [[0] * 2 for _ in range(p_len)]
    
        # starting values
        dp[0][0] = prices[0] * -1
        # dp[0][1] = 0
        dp[1][0] = max(prices[1] * -1, dp[0][0])
        dp[1][1] = max(dp[0][0] + prices[1], dp[0][1])

        # every dp[i][0/1] - maximum profit at that position
        # where 0 is buy/keep, 1 is sell/keep
        for i in range(2, p_len):
            dp[i][0] = max(dp[i - 2][1] - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])

        return max(dp[p_len - 1][0], dp[p_len - 1][1])
