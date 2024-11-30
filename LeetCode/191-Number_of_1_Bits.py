class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while(n != 0):
            n &= (n - 1)
            counter += 1
        
        return counter
    
# Another Solution (Same time complexity)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         counter = 0
#         while(n != 0):
#             if n % 2:
#                 counter += 1
#             n >>= 1
#         return counter