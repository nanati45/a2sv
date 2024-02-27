class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 :
            return False

        if n % 4 == 0:    
            n = n // 4
            return self.isPowerOfFour(n) 
        else:
            return False