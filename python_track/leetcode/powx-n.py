class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0 :
            return 1

        if n < 0:
            n = -1* n
            x = 1/ x

        if n % 2 != 0 :
            m = n // 2
            val = self.myPow(x, m)
            return val * val * x
        else:
            m = n //2
            val = self.myPow(x, m)
            return val * val 
