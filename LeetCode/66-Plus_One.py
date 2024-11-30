# The idea here is simply to reverse the digits array for the
# easier process of adding another entry for the leading 1
# Time complexity - O(n)
# Memory Complexity - O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        digits = digits[::-1]
        propagate = 1
        while(i != len(digits)):
            if digits[i] != 9 and propagate:
                digits[i] += 1
                propagate = 0
            elif digits[i] == 9 and propagate:
                digits[i] = 0
                propagate = 1
            i += 1

        if propagate:
            digits.append(1)
      
        return digits[::-1]
    
# Another Solution (Not Optimal Memory Complexity - O(n))
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         i = len(digits) - 1
#         propagate = 1
#         while(i != -1):
#             if digits[i] != 9 and propagate:
#                 digits[i] += 1
#                 propagate = 0
#             elif digits[i] == 9 and propagate:
#                 digits[i] = 0
#                 propagate = 1
#             i -= 1

#         if propagate:
#             res = [1]
#             res.extend(digits)
#             return res
        
#         return digits