class Solution:
    def maxScore(self, s: str) -> int:
        left =0
        s = [int(i) for i in s]
        l = 0
        right  = sum(s)
        mx = 0
        while l < len(s)-1 :
            if s[l] == 0:
                left +=1
            right -= s[l]
            Sum = right + left
            mx = max(mx, Sum)
            l +=1
            print(left , right)
        return mx     
            