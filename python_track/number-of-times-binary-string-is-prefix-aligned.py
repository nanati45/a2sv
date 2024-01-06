class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:  

        count = 0
        rm = 1
        l = len(flips)
        for i in range(1, l+1):
            rm = max(rm, flips[i-1])
            if i == rm:
                count+=1
    
        return count        

