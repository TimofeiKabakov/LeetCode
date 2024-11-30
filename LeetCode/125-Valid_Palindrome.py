class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        flag = True
 
        while(left < right):
            if not (s[left] >= 'A' and s[left] <= 'Z') and  not (s[left] >= 'a' and s[left] <= 'z') and not (s[left] >= '0' and s[left] <= '9'):
                left += 1
                continue
            
            if  not (s[right] >= 'A' and s[right] <= 'Z') and not (s[right] >= 'a' and s[right] <= 'z') and not (s[right] >= '0' and s[right] <= '9'):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                flag = False
                break

            left += 1
            right -= 1

        return flag
    
# Another Solution (Not Optimal):
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strin = ""
#         for c in s:
#             if c.isalnum():
#                 strin += c.lower()
#         return strin == strin[::-1]