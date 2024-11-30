class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        counter = 0
        while(counter <= 31):
            if n & 1:
                result |= 1
            
            if counter != 31:
                result <<= 1

            n >>= 1
            counter += 1

        return result
    
# Another Solution:
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         result = 0
        
#         left = n
#         for i in range(31, 15, -1):
#             print(i)
#             if left & 1:
#                 result += 2 ** i
#             left >>= 1

#         right = n
#         for i in range(0, 16):
#             print(i)
#             if right & (2 ** 31):
#                 result += 2 ** i
#             right <<= 1

#         return result