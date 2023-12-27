class Solution:
    def largestOddNumber(self, num: str) -> str:
        def is_odd(n):
            if int(n)%2!=0:
                return True
        delimiter=-1
        for i in range(len(num)-1,-1,-1):
            if is_odd(num[i]):
                delimiter=i
                break
        return "" if  delimiter==-1 else num[:delimiter+1]


