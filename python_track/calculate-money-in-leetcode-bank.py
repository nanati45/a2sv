class Solution:
    def totalMoney(self, n: int) -> int:
        c=n%7
        d=n//7
        s = 0
        for i in range(1,d+1):
            s += 7/2*(2*i + 7 -1)
        for i in range(d+1,d+c+1):
            s+=i
        return int(s)
        