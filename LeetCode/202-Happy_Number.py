# Unhappy numbers will eventually fall back to one of the 
# values along the chain and start looping
def sum_digits(x):
    res = 0
    while(x != 0):
        res += (x % 10) ** 2
        x //= 10
    return res

class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        set_v = set()

        while(num != 1):
            num = sum_digits(num)
            if num in set_v:
                return False
            set_v.add(num)
            
        return True