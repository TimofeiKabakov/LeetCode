class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        if n >= 1:
            dp[0] = 1
        if n >= 2:
            dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
    
# Time Complexity: O(n)
# Space Complexity: O(n)