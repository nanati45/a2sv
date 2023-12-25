class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        r=[i for i in range(left,right+1)]
        count=0
        for k in range(len(r)):
            for i in range(len(ranges)):
                c=0
                if r[k] in range(ranges[i][0],ranges[i][1]+1):
                    c+=1
                    break
            count+=c
        print(count)    
        if count<len(r):
            return False
        else:
            return True                         
