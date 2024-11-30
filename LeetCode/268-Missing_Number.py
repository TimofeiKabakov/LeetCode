# XOR opreration is associative: we can xor everything in the 
# "actual" range and then xor it with nums --> everything will 
# cancel out except for the missing number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        entire_range = range(len(nums) + 1)
        
        for n in entire_range:
            xor ^= n
        
        for n in nums:
            xor ^= n

        return xor


# Another Solution (set approach)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         setNums = set(range(n + 1))
#         for num in nums:
#             if num in setNums:
#                 setNums.discard(num)
#         return list(setNums)[0]


# Another Solution (Sum approach):
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums_sum = sum(range(len(nums) + 1))
#         has_zero = 0
        
#         for n in nums:
#             if not n:
#                 has_zero = 1
#             nums_sum -= n

#         if not has_zero:
#             return 0

#         return nums_sum
