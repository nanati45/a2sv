class Solution:
    def largestGoodInteger(self, num: str) -> str:
        same_digit=[]
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                same_digit.append(num[i:i+3])
        same_digit=[int(i) for i in same_digit]
        
        if same_digit:
            m=max(same_digit)
            if m:
                return str(m)
            else:
                return "000"
        else:
            return ""        
           