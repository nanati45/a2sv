class Solution:
    def isUgly(self, n: int) -> bool:
        d = 2 
        if n <= 0 :
            return False
        ugly = [2 , 3, 5 ]
        while d*d <= n :
            if n % d == 0 :
                n //= d
                d = 1
            d += 1
        if n > 1 and n not in ugly:
            return False
        return True            