class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False

        decimals = self.checkDecimals(x)
        
        if(decimals % 2 == 0):
            finish = decimals // 2
        else:
            finish = decimals // 2 + 1
            
        change = x
        
        for n in range(1, finish + 1):
            power = pow(10, decimals - n)
            if((x // power) % 10 != change % 10):
                return False
            change //= 10
                
        return True

    def checkDecimals(self, n: int) -> int:
        counter = 0
        while(n > 0):
            n //= 10
            counter += 1
        return counter
