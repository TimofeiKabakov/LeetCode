class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            mask ^= num

        return mask

# Another Solution (Trivial)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         encountered = {}
#         result = 0
#         for num in nums:
#             if num in encountered:
#                 result -= num
#             else:
#                 encountered[num] = 1
#                 result += num
#         return result