class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for _ in range( n )]
        if n > 0:
            primes[0] = False
        if n > 1:    
            primes[1] = False
        i = 2
        while i <= n - 1:
            if primes[i] :
                j = i * i
                while j <= n - 1 :
                    primes[j] = False
                    j += i
            i += 1
        c = Counter(primes)
        return c[True] 
             