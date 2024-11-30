class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        highest_power_of_two = 1

        for i in range(1, n + 1):
            if i == highest_power_of_two * 2:
                highest_power_of_two *= 2
            dp[i] = 1 + dp[i - highest_power_of_two]

        return dp

# Another Solution (Optimal):
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = [0] * (n + 1)

#         for i in range(n + 1):
#             ans[i] = ans[i >> 1] + i % 2

#         return ans

# Another Solution (Not Optimal):
# def single_num_bits(n):
#     counter = 0
#     while(n != 0):
#         if n & 1:
#             counter += 1
#         n >>= 1
#     return counter

# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res = []

#         for i in range(n + 1):
#             res.append(single_num_bits(i))

#         return res